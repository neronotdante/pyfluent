"""Sphinx documentation configuration file."""
from datetime import datetime
import os
import platform
import subprocess

from ansys_sphinx_theme import ansys_favicon, get_version_match, pyansys_logo_black
from sphinx_gallery.sorting import FileNameSortKey

from ansys.fluent.core import __version__

# -- Project information -----------------------------------------------------

project = "ansys.fluent.core"
copyright = f"(c) {datetime.now().year} ANSYS, Inc. All rights reserved"
author = "ANSYS Inc."
cname = os.getenv("DOCUMENTATION_CNAME", "nocname.com")

# The short X.Y version
release = version = __version__

# -- General configuration ---------------------------------------------------
extensions = [
    "jupyter_sphinx",
    "notfound.extension",
    "numpydoc",
    "autodocsumm",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.coverage",
    "sphinx.ext.doctest",
    "sphinx.ext.extlinks",
    "sphinx.ext.intersphinx",
    "sphinx_autodoc_typehints",
    "sphinx_copybutton",
    "sphinxemoji.sphinxemoji",
]

skip_examples = int(os.getenv("PYFLUENT_SKIP_EXAMPLES_DOC", 0))
if skip_examples:
    pass
else:
    extensions.append("sphinx_gallery.gen_gallery")

typehints_document_rtype = False

# Intersphinx mapping
intersphinx_mapping = {
    "python": ("https://docs.python.org/", None),
    "numpy": ("https://numpy.org/doc/stable", None),
    "pandas": ("https://pandas.pydata.org/pandas-docs/stable", None),
}

# SS01, SS02, SS03, GL08 all need clean up in the code to be reactivated.
# numpydoc configuration
numpydoc_use_plots = True
numpydoc_show_class_members = False
numpydoc_xref_param_type = True
numpydoc_validate = True
numpydoc_validation_checks = {
    "GL06",  # Found unknown section
    "GL07",  # Sections are in the wrong order.
    "GL08",  # The object does not have a docstring
    "GL09",  # Deprecation warning should precede extended summary
    "GL10",  # reST directives {directives} must be followed by two colons
    "SS01",  # No summary found
    "SS02",  # Summary does not start with a capital letter
    "SS03",  # Summary does not end with a period
    "SS04",  # Summary contains heading whitespaces
    # "SS05", # Summary must start with infinitive verb, not third person
    "RT02",  # The first line of the Returns section should contain only the
    # type, unless multiple values are being returned"
}
numpydoc_validation_exclude = {
    "ansys.fluent.core.solver.settings_231.",
    "ansys.fluent.core.solver.settings_232.",
    "ansys.fluent.core.solver.settings_241.",
    "ansys.fluent.core.services.batch_ops.BatchOps.__init__",
}

# Favicon
html_favicon = ansys_favicon

# static path
html_static_path = ["_static"]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The suffix(es) of source filenames.
source_suffix = ".rst"

# The master toctree document.
master_doc = "index"

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = "en"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build"]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False

# Copy button customization ---------------------------------------------------
# exclude traditional Python prompts from the copied code
copybutton_prompt_text = r">>> ?|\.\.\. "
copybutton_prompt_is_regexp = True


def _stop_fluent_container(gallery_conf, fname):
    try:
        is_linux = platform.system() == "Linux"
        container_names = (
            subprocess.check_output(
                "docker container ls --format {{.Names}}", shell=is_linux
            )
            .decode("utf-8")
            .strip()
            .split()
        )
        for container_name in container_names:
            subprocess.run(f"docker stop {container_name}", shell=is_linux)
    except Exception:
        pass


# -- Sphinx Gallery Options ---------------------------------------------------
sphinx_gallery_conf = {
    # convert rst to md for ipynb
    # "pypandoc": True,
    # path to your examples scripts
    "examples_dirs": ["../../examples/"],
    # path where to save gallery generated examples
    "gallery_dirs": ["examples"],
    # Pattern to search for example files
    "filename_pattern": r"\.py",
    # Remove the "Download all examples" button from the top level gallery
    "download_all_examples": False,
    # Sort gallery example by file name instead of number of lines (default)
    "within_subsection_order": FileNameSortKey,
    # directory where function granular galleries are stored
    "backreferences_dir": None,
    # Modules for which function level galleries are created.  In
    "doc_module": "ansys-fluent-core",
    "ignore_pattern": "flycheck*",
    "thumbnail_size": (350, 350),
    "reset_modules_order": "after",
    "reset_modules": (_stop_fluent_container),
    "capture_repr": (),
    "remove_config_comments": True,
    "abort_on_example_error": True,
}


# -- Options for HTML output -------------------------------------------------
html_short_title = html_title = "PyFluent"
html_theme = "ansys_sphinx_theme"
html_logo = pyansys_logo_black
html_theme_options = {
    "github_url": "https://github.com/ansys/pyfluent",
    "show_prev_next": False,
    "show_breadcrumbs": True,
    "additional_breadcrumbs": [
        ("PyAnsys", "https://docs.pyansys.com/"),
    ],
    "icon_links": [
        {
            "name": "Support",
            "url": "https://github.com/ansys/pyfluent/discussions",
            "icon": "fa fa-comment fa-fw",
        },
    ],
    "switcher": {
        "json_url": f"https://{cname}/versions.json",
        "version_match": get_version_match(__version__),
    },
    "use_meilisearch": {
        "api_key": os.getenv("MEILISEARCH_PUBLIC_API_KEY", ""),
        "index_uids": {
            f"pyfluent-v{get_version_match(__version__).replace('.', '-')}": "PyFluent",
        },
    },
    "navbar_end": ["version-switcher", "theme-switcher", "navbar-icon-links"],
    "navigation_depth": -1,
    "collapse_navigation": True,
}

# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = "pyfluentdoc"


# -- Options for LaTeX output ------------------------------------------------
latex_elements = {}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (
        master_doc,
        f"pyfluent-Documentation-{__version__}.tex",
        "ansys.fluent.core Documentation",
        author,
        "manual",
    ),
]


# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (
        master_doc,
        "ansys.fluent.core",
        "ansys.fluent.core Documentation",
        [author],
        1,
    )
]


# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (
        master_doc,
        "ansys.fluent.core",
        "ansys.fluent.core Documentation",
        author,
        "ansys.fluent.core",
        "Pythonic interface for Fluent using gRPC",
        "Engineering Software",
    ),
]


# -- Options for Epub output -------------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#
# epub_identifier = ''

# A unique identification for the text.
#
# epub_uid = ''

# A list of files that should not be packed into the epub file.
epub_exclude_files = ["search.html"]

import dash
from app_defn import app
from dash import dcc, html
import dash_bootstrap_components as dbc
from dash import Input, Output, State, ALL
from flask import request
from sessions_manager import SessionsManager


from settings_property_editor import SettingsPropertyEditor
from local_property_editor import LocalPropertyEditor
from post_windows import MonitorWindow, GraphicsWindowCollection

setting1 = SettingsPropertyEditor(app, SessionsManager)
setting2 = SettingsPropertyEditor(app, SessionsManager)
setting3 = SettingsPropertyEditor(app, SessionsManager)
local_editor = LocalPropertyEditor(app, SessionsManager)


def get_post_objects(user_id, session_id):
    return dbc.Row(
        [
            dbc.Col(
                [
                    dcc.Dropdown(
                        id="post-object-type",
                        options=["Mesh", "Surface", "Contour", "Vector"],
                        value="Contour",
                        style={"padding": "10px 5px 5px 5px"},
                    ),
                    html.Div(id="post-object-container"),
                ],
                width="auto",
                style={"width": "350px"},
            ),
            dbc.Col([GraphicsWindowCollection(app, user_id, session_id, SessionsManager)()]),
        ]
    )


def get_setup_objects(user_id, session_id):
    return dbc.Row(
        [
            dbc.Col(
                [
                    setting1(user_id, session_id, "remote:setup/models/viscous:"),
                    setting2(
                        user_id,
                        session_id,
                        "remote:solution/initialization:",
                        ["standard-initialize"],
                    ),
                    setting3(
                        user_id,
                        session_id,
                        "remote:solution/run_calculation:",
                        ["iterate"],
                    ),
                ],
                width="auto",
                style={"width": "350px", "padding": "10px"},
            ),
            dbc.Col([MonitorWindow(app, user_id, session_id, SessionsManager)()]),
        ],
        style={"padding": "10px"},
    )


def app_layout():
    user_id = request.authorization["username"]
    session_id = "session-0"
    sessions_manager = SessionsManager(app, app_layout.user_id, session_id)
    sessions_manager.add_session("53583", None)

    return dbc.Container(
        fluid=True,
        children=[
            html.Data(id="session-id", value="session-0"),
            dbc.Row(
                html.Div(
                    [
                        html.Img(
                            src="/assets/pyansys.png",
                            style={"height": "35px"},
                        ),
                        html.P(
                            html.B("PyFluent Web Client"),
                            style={
                                "font": "24px 'Segoe UI'",
                                "padding": "0px 0px 0px 20px",
                            },
                        ),
                    ],
                    style={"display": "flex", "flex-direction": "row", "border": "1px soild lightgray"},
                ),
            ),
            dbc.Row(
                [
                    dbc.Tabs(
                        [
                            dbc.Tab(
                                label="Setup",
                                tab_id="setup",
                            ),
                            dbc.Tab(label="Post", tab_id="post"),
                        ],
                        id="demo-app-tabs",
                        active_tab="setup",
                    ),
                    html.Div(
                        id="demo-app-tab-content",
                    ),
                ],
            ),
        ],
        style={"font": "14px 'Segoe UI'", "border": "1px soild lightgray"},
    )


@app.callback(
    Output("post-object-container", "children"),
    Input("post-object-type", "value"),
    State("connection-id", "data"),
    State("session-id", "value"),
)
def render_widget(post_object_type, user_id, session_id):
    return local_editor(user_id, session_id, f"local:{post_object_type}:0")


@app.callback(
    Output("demo-app-tab-content", "children"),
    Input("demo-app-tabs", "active_tab"),
    Input("connection-id", "data"),
    Input("session-id", "value"),
)
def render_tab_content(active_tab, user_id, session_id):

    if active_tab == "setup":
        return get_setup_objects(user_id, session_id)
    if active_tab == "post":
        return get_post_objects(user_id, session_id)

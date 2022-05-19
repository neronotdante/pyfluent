# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import ansys.api.fluent.v0.field_data_pb2 as field__data__pb2


class FieldDataStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetFields = channel.unary_stream(
                '/grpcRemoting.FieldData/GetFields',
                request_serializer=field__data__pb2.GetFieldsRequest.SerializeToString,
                response_deserializer=field__data__pb2.GetFieldsResponse.FromString,
                )
        self.GetRange = channel.unary_unary(
                '/grpcRemoting.FieldData/GetRange',
                request_serializer=field__data__pb2.GetRangeRequest.SerializeToString,
                response_deserializer=field__data__pb2.GetRangeResponse.FromString,
                )
        self.GetSurfacesInfo = channel.unary_unary(
                '/grpcRemoting.FieldData/GetSurfacesInfo',
                request_serializer=field__data__pb2.GetSurfacesInfoRequest.SerializeToString,
                response_deserializer=field__data__pb2.GetSurfacesInfoResponse.FromString,
                )
        self.GetVectorFieldsInfo = channel.unary_unary(
                '/grpcRemoting.FieldData/GetVectorFieldsInfo',
                request_serializer=field__data__pb2.GetVectorFieldsInfoRequest.SerializeToString,
                response_deserializer=field__data__pb2.GetVectorFieldsInfoResponse.FromString,
                )
        self.GetFieldsInfo = channel.unary_unary(
                '/grpcRemoting.FieldData/GetFieldsInfo',
                request_serializer=field__data__pb2.GetFieldsInfoRequest.SerializeToString,
                response_deserializer=field__data__pb2.GetFieldsInfoResponse.FromString,
                )
        self.GetSurfaces = channel.unary_stream(
                '/grpcRemoting.FieldData/GetSurfaces',
                request_serializer=field__data__pb2.GetSurfacesRequest.SerializeToString,
                response_deserializer=field__data__pb2.GetSurfacesResponse.FromString,
                )
        self.GetScalarField = channel.unary_stream(
                '/grpcRemoting.FieldData/GetScalarField',
                request_serializer=field__data__pb2.GetScalarFieldRequest.SerializeToString,
                response_deserializer=field__data__pb2.GetScalarFieldResponse.FromString,
                )
        self.GetVectorField = channel.unary_stream(
                '/grpcRemoting.FieldData/GetVectorField',
                request_serializer=field__data__pb2.GetVectorFieldRequest.SerializeToString,
                response_deserializer=field__data__pb2.GetVectorFieldResponse.FromString,
                )
        self.GetPathlinesField = channel.unary_stream(
                '/grpcRemoting.FieldData/GetPathlinesField',
                request_serializer=field__data__pb2.GetPathlinesFieldRequest.SerializeToString,
                response_deserializer=field__data__pb2.GetPathlinesFieldResponse.FromString,
                )
        self.GetParticleTracksField = channel.unary_stream(
                '/grpcRemoting.FieldData/GetParticleTracksField',
                request_serializer=field__data__pb2.GetParticleTracksFieldRequest.SerializeToString,
                response_deserializer=field__data__pb2.GetParticleTracksFieldResponse.FromString,
                )
        self.IsBoundaryValuesOn = channel.unary_unary(
                '/grpcRemoting.FieldData/IsBoundaryValuesOn',
                request_serializer=field__data__pb2.IsBoundaryValuesOnRequest.SerializeToString,
                response_deserializer=field__data__pb2.IsBoundaryValuesOnResponse.FromString,
                )


class FieldDataServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetFields(self, request, context):
        """Get fields e.g. scalar, vector, surfaces etc in a single request.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetRange(self, request, context):
        """Get scalar field range.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetSurfacesInfo(self, request, context):
        """Get surfaces info.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetVectorFieldsInfo(self, request, context):
        """Get vector fields info.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetFieldsInfo(self, request, context):
        """Get scalar fields info.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetSurfaces(self, request, context):
        """Get surfaces data.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetScalarField(self, request, context):
        """Get scalar field data.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetVectorField(self, request, context):
        """Get vector field data.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetPathlinesField(self, request, context):
        """Get pathlines field data.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetParticleTracksField(self, request, context):
        """Get particle tracks field data.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def IsBoundaryValuesOn(self, request, context):
        """Check if boundary values are on.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_FieldDataServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetFields': grpc.unary_stream_rpc_method_handler(
                    servicer.GetFields,
                    request_deserializer=field__data__pb2.GetFieldsRequest.FromString,
                    response_serializer=field__data__pb2.GetFieldsResponse.SerializeToString,
            ),
            'GetRange': grpc.unary_unary_rpc_method_handler(
                    servicer.GetRange,
                    request_deserializer=field__data__pb2.GetRangeRequest.FromString,
                    response_serializer=field__data__pb2.GetRangeResponse.SerializeToString,
            ),
            'GetSurfacesInfo': grpc.unary_unary_rpc_method_handler(
                    servicer.GetSurfacesInfo,
                    request_deserializer=field__data__pb2.GetSurfacesInfoRequest.FromString,
                    response_serializer=field__data__pb2.GetSurfacesInfoResponse.SerializeToString,
            ),
            'GetVectorFieldsInfo': grpc.unary_unary_rpc_method_handler(
                    servicer.GetVectorFieldsInfo,
                    request_deserializer=field__data__pb2.GetVectorFieldsInfoRequest.FromString,
                    response_serializer=field__data__pb2.GetVectorFieldsInfoResponse.SerializeToString,
            ),
            'GetFieldsInfo': grpc.unary_unary_rpc_method_handler(
                    servicer.GetFieldsInfo,
                    request_deserializer=field__data__pb2.GetFieldsInfoRequest.FromString,
                    response_serializer=field__data__pb2.GetFieldsInfoResponse.SerializeToString,
            ),
            'GetSurfaces': grpc.unary_stream_rpc_method_handler(
                    servicer.GetSurfaces,
                    request_deserializer=field__data__pb2.GetSurfacesRequest.FromString,
                    response_serializer=field__data__pb2.GetSurfacesResponse.SerializeToString,
            ),
            'GetScalarField': grpc.unary_stream_rpc_method_handler(
                    servicer.GetScalarField,
                    request_deserializer=field__data__pb2.GetScalarFieldRequest.FromString,
                    response_serializer=field__data__pb2.GetScalarFieldResponse.SerializeToString,
            ),
            'GetVectorField': grpc.unary_stream_rpc_method_handler(
                    servicer.GetVectorField,
                    request_deserializer=field__data__pb2.GetVectorFieldRequest.FromString,
                    response_serializer=field__data__pb2.GetVectorFieldResponse.SerializeToString,
            ),
            'GetPathlinesField': grpc.unary_stream_rpc_method_handler(
                    servicer.GetPathlinesField,
                    request_deserializer=field__data__pb2.GetPathlinesFieldRequest.FromString,
                    response_serializer=field__data__pb2.GetPathlinesFieldResponse.SerializeToString,
            ),
            'GetParticleTracksField': grpc.unary_stream_rpc_method_handler(
                    servicer.GetParticleTracksField,
                    request_deserializer=field__data__pb2.GetParticleTracksFieldRequest.FromString,
                    response_serializer=field__data__pb2.GetParticleTracksFieldResponse.SerializeToString,
            ),
            'IsBoundaryValuesOn': grpc.unary_unary_rpc_method_handler(
                    servicer.IsBoundaryValuesOn,
                    request_deserializer=field__data__pb2.IsBoundaryValuesOnRequest.FromString,
                    response_serializer=field__data__pb2.IsBoundaryValuesOnResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'grpcRemoting.FieldData', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class FieldData(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetFields(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/grpcRemoting.FieldData/GetFields',
            field__data__pb2.GetFieldsRequest.SerializeToString,
            field__data__pb2.GetFieldsResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetRange(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/grpcRemoting.FieldData/GetRange',
            field__data__pb2.GetRangeRequest.SerializeToString,
            field__data__pb2.GetRangeResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetSurfacesInfo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/grpcRemoting.FieldData/GetSurfacesInfo',
            field__data__pb2.GetSurfacesInfoRequest.SerializeToString,
            field__data__pb2.GetSurfacesInfoResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetVectorFieldsInfo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/grpcRemoting.FieldData/GetVectorFieldsInfo',
            field__data__pb2.GetVectorFieldsInfoRequest.SerializeToString,
            field__data__pb2.GetVectorFieldsInfoResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetFieldsInfo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/grpcRemoting.FieldData/GetFieldsInfo',
            field__data__pb2.GetFieldsInfoRequest.SerializeToString,
            field__data__pb2.GetFieldsInfoResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetSurfaces(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/grpcRemoting.FieldData/GetSurfaces',
            field__data__pb2.GetSurfacesRequest.SerializeToString,
            field__data__pb2.GetSurfacesResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetScalarField(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/grpcRemoting.FieldData/GetScalarField',
            field__data__pb2.GetScalarFieldRequest.SerializeToString,
            field__data__pb2.GetScalarFieldResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetVectorField(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/grpcRemoting.FieldData/GetVectorField',
            field__data__pb2.GetVectorFieldRequest.SerializeToString,
            field__data__pb2.GetVectorFieldResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetPathlinesField(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/grpcRemoting.FieldData/GetPathlinesField',
            field__data__pb2.GetPathlinesFieldRequest.SerializeToString,
            field__data__pb2.GetPathlinesFieldResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetParticleTracksField(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/grpcRemoting.FieldData/GetParticleTracksField',
            field__data__pb2.GetParticleTracksFieldRequest.SerializeToString,
            field__data__pb2.GetParticleTracksFieldResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def IsBoundaryValuesOn(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/grpcRemoting.FieldData/IsBoundaryValuesOn',
            field__data__pb2.IsBoundaryValuesOnRequest.SerializeToString,
            field__data__pb2.IsBoundaryValuesOnResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import backend_nvme_tcp_pb2 as backend__nvme__tcp__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


class NvmeRemoteControllerServiceStub(object):
    """Back End (network-facing) APIs. NVMe/TCP and NVMe/RoCEv2 protocols are covered by this service.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateNvmeRemoteController = channel.unary_unary(
                '/opi_api.storage.v1.NvmeRemoteControllerService/CreateNvmeRemoteController',
                request_serializer=backend__nvme__tcp__pb2.CreateNvmeRemoteControllerRequest.SerializeToString,
                response_deserializer=backend__nvme__tcp__pb2.NvmeRemoteController.FromString,
                )
        self.DeleteNvmeRemoteController = channel.unary_unary(
                '/opi_api.storage.v1.NvmeRemoteControllerService/DeleteNvmeRemoteController',
                request_serializer=backend__nvme__tcp__pb2.DeleteNvmeRemoteControllerRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.UpdateNvmeRemoteController = channel.unary_unary(
                '/opi_api.storage.v1.NvmeRemoteControllerService/UpdateNvmeRemoteController',
                request_serializer=backend__nvme__tcp__pb2.UpdateNvmeRemoteControllerRequest.SerializeToString,
                response_deserializer=backend__nvme__tcp__pb2.NvmeRemoteController.FromString,
                )
        self.ListNvmeRemoteControllers = channel.unary_unary(
                '/opi_api.storage.v1.NvmeRemoteControllerService/ListNvmeRemoteControllers',
                request_serializer=backend__nvme__tcp__pb2.ListNvmeRemoteControllersRequest.SerializeToString,
                response_deserializer=backend__nvme__tcp__pb2.ListNvmeRemoteControllersResponse.FromString,
                )
        self.GetNvmeRemoteController = channel.unary_unary(
                '/opi_api.storage.v1.NvmeRemoteControllerService/GetNvmeRemoteController',
                request_serializer=backend__nvme__tcp__pb2.GetNvmeRemoteControllerRequest.SerializeToString,
                response_deserializer=backend__nvme__tcp__pb2.NvmeRemoteController.FromString,
                )
        self.NvmeRemoteControllerReset = channel.unary_unary(
                '/opi_api.storage.v1.NvmeRemoteControllerService/NvmeRemoteControllerReset',
                request_serializer=backend__nvme__tcp__pb2.NvmeRemoteControllerResetRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.NvmeRemoteControllerStats = channel.unary_unary(
                '/opi_api.storage.v1.NvmeRemoteControllerService/NvmeRemoteControllerStats',
                request_serializer=backend__nvme__tcp__pb2.NvmeRemoteControllerStatsRequest.SerializeToString,
                response_deserializer=backend__nvme__tcp__pb2.NvmeRemoteControllerStatsResponse.FromString,
                )
        self.ListNvmeRemoteNamespaces = channel.unary_unary(
                '/opi_api.storage.v1.NvmeRemoteControllerService/ListNvmeRemoteNamespaces',
                request_serializer=backend__nvme__tcp__pb2.ListNvmeRemoteNamespacesRequest.SerializeToString,
                response_deserializer=backend__nvme__tcp__pb2.ListNvmeRemoteNamespacesResponse.FromString,
                )
        self.CreateNvmePath = channel.unary_unary(
                '/opi_api.storage.v1.NvmeRemoteControllerService/CreateNvmePath',
                request_serializer=backend__nvme__tcp__pb2.CreateNvmePathRequest.SerializeToString,
                response_deserializer=backend__nvme__tcp__pb2.NvmePath.FromString,
                )
        self.DeleteNvmePath = channel.unary_unary(
                '/opi_api.storage.v1.NvmeRemoteControllerService/DeleteNvmePath',
                request_serializer=backend__nvme__tcp__pb2.DeleteNvmePathRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.UpdateNvmePath = channel.unary_unary(
                '/opi_api.storage.v1.NvmeRemoteControllerService/UpdateNvmePath',
                request_serializer=backend__nvme__tcp__pb2.UpdateNvmePathRequest.SerializeToString,
                response_deserializer=backend__nvme__tcp__pb2.NvmePath.FromString,
                )
        self.ListNvmePaths = channel.unary_unary(
                '/opi_api.storage.v1.NvmeRemoteControllerService/ListNvmePaths',
                request_serializer=backend__nvme__tcp__pb2.ListNvmePathsRequest.SerializeToString,
                response_deserializer=backend__nvme__tcp__pb2.ListNvmePathsResponse.FromString,
                )
        self.GetNvmePath = channel.unary_unary(
                '/opi_api.storage.v1.NvmeRemoteControllerService/GetNvmePath',
                request_serializer=backend__nvme__tcp__pb2.GetNvmePathRequest.SerializeToString,
                response_deserializer=backend__nvme__tcp__pb2.NvmePath.FromString,
                )
        self.NvmePathStats = channel.unary_unary(
                '/opi_api.storage.v1.NvmeRemoteControllerService/NvmePathStats',
                request_serializer=backend__nvme__tcp__pb2.NvmePathStatsRequest.SerializeToString,
                response_deserializer=backend__nvme__tcp__pb2.NvmePathStatsResponse.FromString,
                )


class NvmeRemoteControllerServiceServicer(object):
    """Back End (network-facing) APIs. NVMe/TCP and NVMe/RoCEv2 protocols are covered by this service.
    """

    def CreateNvmeRemoteController(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteNvmeRemoteController(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateNvmeRemoteController(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListNvmeRemoteControllers(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetNvmeRemoteController(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def NvmeRemoteControllerReset(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def NvmeRemoteControllerStats(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListNvmeRemoteNamespaces(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateNvmePath(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteNvmePath(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateNvmePath(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListNvmePaths(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetNvmePath(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def NvmePathStats(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_NvmeRemoteControllerServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateNvmeRemoteController': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateNvmeRemoteController,
                    request_deserializer=backend__nvme__tcp__pb2.CreateNvmeRemoteControllerRequest.FromString,
                    response_serializer=backend__nvme__tcp__pb2.NvmeRemoteController.SerializeToString,
            ),
            'DeleteNvmeRemoteController': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteNvmeRemoteController,
                    request_deserializer=backend__nvme__tcp__pb2.DeleteNvmeRemoteControllerRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'UpdateNvmeRemoteController': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateNvmeRemoteController,
                    request_deserializer=backend__nvme__tcp__pb2.UpdateNvmeRemoteControllerRequest.FromString,
                    response_serializer=backend__nvme__tcp__pb2.NvmeRemoteController.SerializeToString,
            ),
            'ListNvmeRemoteControllers': grpc.unary_unary_rpc_method_handler(
                    servicer.ListNvmeRemoteControllers,
                    request_deserializer=backend__nvme__tcp__pb2.ListNvmeRemoteControllersRequest.FromString,
                    response_serializer=backend__nvme__tcp__pb2.ListNvmeRemoteControllersResponse.SerializeToString,
            ),
            'GetNvmeRemoteController': grpc.unary_unary_rpc_method_handler(
                    servicer.GetNvmeRemoteController,
                    request_deserializer=backend__nvme__tcp__pb2.GetNvmeRemoteControllerRequest.FromString,
                    response_serializer=backend__nvme__tcp__pb2.NvmeRemoteController.SerializeToString,
            ),
            'NvmeRemoteControllerReset': grpc.unary_unary_rpc_method_handler(
                    servicer.NvmeRemoteControllerReset,
                    request_deserializer=backend__nvme__tcp__pb2.NvmeRemoteControllerResetRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'NvmeRemoteControllerStats': grpc.unary_unary_rpc_method_handler(
                    servicer.NvmeRemoteControllerStats,
                    request_deserializer=backend__nvme__tcp__pb2.NvmeRemoteControllerStatsRequest.FromString,
                    response_serializer=backend__nvme__tcp__pb2.NvmeRemoteControllerStatsResponse.SerializeToString,
            ),
            'ListNvmeRemoteNamespaces': grpc.unary_unary_rpc_method_handler(
                    servicer.ListNvmeRemoteNamespaces,
                    request_deserializer=backend__nvme__tcp__pb2.ListNvmeRemoteNamespacesRequest.FromString,
                    response_serializer=backend__nvme__tcp__pb2.ListNvmeRemoteNamespacesResponse.SerializeToString,
            ),
            'CreateNvmePath': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateNvmePath,
                    request_deserializer=backend__nvme__tcp__pb2.CreateNvmePathRequest.FromString,
                    response_serializer=backend__nvme__tcp__pb2.NvmePath.SerializeToString,
            ),
            'DeleteNvmePath': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteNvmePath,
                    request_deserializer=backend__nvme__tcp__pb2.DeleteNvmePathRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'UpdateNvmePath': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateNvmePath,
                    request_deserializer=backend__nvme__tcp__pb2.UpdateNvmePathRequest.FromString,
                    response_serializer=backend__nvme__tcp__pb2.NvmePath.SerializeToString,
            ),
            'ListNvmePaths': grpc.unary_unary_rpc_method_handler(
                    servicer.ListNvmePaths,
                    request_deserializer=backend__nvme__tcp__pb2.ListNvmePathsRequest.FromString,
                    response_serializer=backend__nvme__tcp__pb2.ListNvmePathsResponse.SerializeToString,
            ),
            'GetNvmePath': grpc.unary_unary_rpc_method_handler(
                    servicer.GetNvmePath,
                    request_deserializer=backend__nvme__tcp__pb2.GetNvmePathRequest.FromString,
                    response_serializer=backend__nvme__tcp__pb2.NvmePath.SerializeToString,
            ),
            'NvmePathStats': grpc.unary_unary_rpc_method_handler(
                    servicer.NvmePathStats,
                    request_deserializer=backend__nvme__tcp__pb2.NvmePathStatsRequest.FromString,
                    response_serializer=backend__nvme__tcp__pb2.NvmePathStatsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'opi_api.storage.v1.NvmeRemoteControllerService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class NvmeRemoteControllerService(object):
    """Back End (network-facing) APIs. NVMe/TCP and NVMe/RoCEv2 protocols are covered by this service.
    """

    @staticmethod
    def CreateNvmeRemoteController(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/opi_api.storage.v1.NvmeRemoteControllerService/CreateNvmeRemoteController',
            backend__nvme__tcp__pb2.CreateNvmeRemoteControllerRequest.SerializeToString,
            backend__nvme__tcp__pb2.NvmeRemoteController.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteNvmeRemoteController(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/opi_api.storage.v1.NvmeRemoteControllerService/DeleteNvmeRemoteController',
            backend__nvme__tcp__pb2.DeleteNvmeRemoteControllerRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateNvmeRemoteController(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/opi_api.storage.v1.NvmeRemoteControllerService/UpdateNvmeRemoteController',
            backend__nvme__tcp__pb2.UpdateNvmeRemoteControllerRequest.SerializeToString,
            backend__nvme__tcp__pb2.NvmeRemoteController.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListNvmeRemoteControllers(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/opi_api.storage.v1.NvmeRemoteControllerService/ListNvmeRemoteControllers',
            backend__nvme__tcp__pb2.ListNvmeRemoteControllersRequest.SerializeToString,
            backend__nvme__tcp__pb2.ListNvmeRemoteControllersResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetNvmeRemoteController(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/opi_api.storage.v1.NvmeRemoteControllerService/GetNvmeRemoteController',
            backend__nvme__tcp__pb2.GetNvmeRemoteControllerRequest.SerializeToString,
            backend__nvme__tcp__pb2.NvmeRemoteController.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def NvmeRemoteControllerReset(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/opi_api.storage.v1.NvmeRemoteControllerService/NvmeRemoteControllerReset',
            backend__nvme__tcp__pb2.NvmeRemoteControllerResetRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def NvmeRemoteControllerStats(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/opi_api.storage.v1.NvmeRemoteControllerService/NvmeRemoteControllerStats',
            backend__nvme__tcp__pb2.NvmeRemoteControllerStatsRequest.SerializeToString,
            backend__nvme__tcp__pb2.NvmeRemoteControllerStatsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListNvmeRemoteNamespaces(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/opi_api.storage.v1.NvmeRemoteControllerService/ListNvmeRemoteNamespaces',
            backend__nvme__tcp__pb2.ListNvmeRemoteNamespacesRequest.SerializeToString,
            backend__nvme__tcp__pb2.ListNvmeRemoteNamespacesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateNvmePath(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/opi_api.storage.v1.NvmeRemoteControllerService/CreateNvmePath',
            backend__nvme__tcp__pb2.CreateNvmePathRequest.SerializeToString,
            backend__nvme__tcp__pb2.NvmePath.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteNvmePath(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/opi_api.storage.v1.NvmeRemoteControllerService/DeleteNvmePath',
            backend__nvme__tcp__pb2.DeleteNvmePathRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateNvmePath(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/opi_api.storage.v1.NvmeRemoteControllerService/UpdateNvmePath',
            backend__nvme__tcp__pb2.UpdateNvmePathRequest.SerializeToString,
            backend__nvme__tcp__pb2.NvmePath.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListNvmePaths(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/opi_api.storage.v1.NvmeRemoteControllerService/ListNvmePaths',
            backend__nvme__tcp__pb2.ListNvmePathsRequest.SerializeToString,
            backend__nvme__tcp__pb2.ListNvmePathsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetNvmePath(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/opi_api.storage.v1.NvmeRemoteControllerService/GetNvmePath',
            backend__nvme__tcp__pb2.GetNvmePathRequest.SerializeToString,
            backend__nvme__tcp__pb2.NvmePath.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def NvmePathStats(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/opi_api.storage.v1.NvmeRemoteControllerService/NvmePathStats',
            backend__nvme__tcp__pb2.NvmePathStatsRequest.SerializeToString,
            backend__nvme__tcp__pb2.NvmePathStatsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

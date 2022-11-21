# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import admin_pb2 as admin__pb2


class AdminStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.inserirCliente = channel.unary_unary(
                '/Admin/inserirCliente',
                request_serializer=admin__pb2.inserirClienteRequest.SerializeToString,
                response_deserializer=admin__pb2.inserirClienteReply.FromString,
                )
        self.modificarCliente = channel.unary_unary(
                '/Admin/modificarCliente',
                request_serializer=admin__pb2.modificarClienteRequest.SerializeToString,
                response_deserializer=admin__pb2.modificarClienteReply.FromString,
                )
        self.recuperarCliente = channel.unary_unary(
                '/Admin/recuperarCliente',
                request_serializer=admin__pb2.recuperarClienteRequest.SerializeToString,
                response_deserializer=admin__pb2.recuperarClienteReply.FromString,
                )
        self.apagarCliente = channel.unary_unary(
                '/Admin/apagarCliente',
                request_serializer=admin__pb2.apagarClienteRequest.SerializeToString,
                response_deserializer=admin__pb2.apagarClienteReply.FromString,
                )
        self.inserirProduto = channel.unary_unary(
                '/Admin/inserirProduto',
                request_serializer=admin__pb2.inserirProdutoRequest.SerializeToString,
                response_deserializer=admin__pb2.inserirProdutoReply.FromString,
                )
        self.modificarProduto = channel.unary_unary(
                '/Admin/modificarProduto',
                request_serializer=admin__pb2.modificarProdutoRequest.SerializeToString,
                response_deserializer=admin__pb2.modificarProdutoReply.FromString,
                )
        self.recuperarProduto = channel.unary_unary(
                '/Admin/recuperarProduto',
                request_serializer=admin__pb2.recuperarProdutoRequest.SerializeToString,
                response_deserializer=admin__pb2.recuperarProdutoReply.FromString,
                )
        self.apagarProduto = channel.unary_unary(
                '/Admin/apagarProduto',
                request_serializer=admin__pb2.apagarProdutoRequest.SerializeToString,
                response_deserializer=admin__pb2.apagarProdutoReply.FromString,
                )


class AdminServicer(object):
    """Missing associated documentation comment in .proto file."""

    def inserirCliente(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def modificarCliente(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def recuperarCliente(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def apagarCliente(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def inserirProduto(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def modificarProduto(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def recuperarProduto(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def apagarProduto(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AdminServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'inserirCliente': grpc.unary_unary_rpc_method_handler(
                    servicer.inserirCliente,
                    request_deserializer=admin__pb2.inserirClienteRequest.FromString,
                    response_serializer=admin__pb2.inserirClienteReply.SerializeToString,
            ),
            'modificarCliente': grpc.unary_unary_rpc_method_handler(
                    servicer.modificarCliente,
                    request_deserializer=admin__pb2.modificarClienteRequest.FromString,
                    response_serializer=admin__pb2.modificarClienteReply.SerializeToString,
            ),
            'recuperarCliente': grpc.unary_unary_rpc_method_handler(
                    servicer.recuperarCliente,
                    request_deserializer=admin__pb2.recuperarClienteRequest.FromString,
                    response_serializer=admin__pb2.recuperarClienteReply.SerializeToString,
            ),
            'apagarCliente': grpc.unary_unary_rpc_method_handler(
                    servicer.apagarCliente,
                    request_deserializer=admin__pb2.apagarClienteRequest.FromString,
                    response_serializer=admin__pb2.apagarClienteReply.SerializeToString,
            ),
            'inserirProduto': grpc.unary_unary_rpc_method_handler(
                    servicer.inserirProduto,
                    request_deserializer=admin__pb2.inserirProdutoRequest.FromString,
                    response_serializer=admin__pb2.inserirProdutoReply.SerializeToString,
            ),
            'modificarProduto': grpc.unary_unary_rpc_method_handler(
                    servicer.modificarProduto,
                    request_deserializer=admin__pb2.modificarProdutoRequest.FromString,
                    response_serializer=admin__pb2.modificarProdutoReply.SerializeToString,
            ),
            'recuperarProduto': grpc.unary_unary_rpc_method_handler(
                    servicer.recuperarProduto,
                    request_deserializer=admin__pb2.recuperarProdutoRequest.FromString,
                    response_serializer=admin__pb2.recuperarProdutoReply.SerializeToString,
            ),
            'apagarProduto': grpc.unary_unary_rpc_method_handler(
                    servicer.apagarProduto,
                    request_deserializer=admin__pb2.apagarProdutoRequest.FromString,
                    response_serializer=admin__pb2.apagarProdutoReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Admin', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Admin(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def inserirCliente(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Admin/inserirCliente',
            admin__pb2.inserirClienteRequest.SerializeToString,
            admin__pb2.inserirClienteReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def modificarCliente(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Admin/modificarCliente',
            admin__pb2.modificarClienteRequest.SerializeToString,
            admin__pb2.modificarClienteReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def recuperarCliente(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Admin/recuperarCliente',
            admin__pb2.recuperarClienteRequest.SerializeToString,
            admin__pb2.recuperarClienteReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def apagarCliente(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Admin/apagarCliente',
            admin__pb2.apagarClienteRequest.SerializeToString,
            admin__pb2.apagarClienteReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def inserirProduto(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Admin/inserirProduto',
            admin__pb2.inserirProdutoRequest.SerializeToString,
            admin__pb2.inserirProdutoReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def modificarProduto(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Admin/modificarProduto',
            admin__pb2.modificarProdutoRequest.SerializeToString,
            admin__pb2.modificarProdutoReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def recuperarProduto(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Admin/recuperarProduto',
            admin__pb2.recuperarProdutoRequest.SerializeToString,
            admin__pb2.recuperarProdutoReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def apagarProduto(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Admin/apagarProduto',
            admin__pb2.apagarProdutoRequest.SerializeToString,
            admin__pb2.apagarProdutoReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

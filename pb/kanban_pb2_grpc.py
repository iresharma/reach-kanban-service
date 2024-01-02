# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import pb.kanban_pb2 as kanban__pb2


class KanbanPackageStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.InitializeKanban = channel.unary_unary(
                '/kanban_package.KanbanPackage/InitializeKanban',
                request_serializer=kanban__pb2.CreateKanbanRequest.SerializeToString,
                response_deserializer=kanban__pb2.BoardResponse.FromString,
                )
        self.AddLabel = channel.unary_unary(
                '/kanban_package.KanbanPackage/AddLabel',
                request_serializer=kanban__pb2.LabelRequest.SerializeToString,
                response_deserializer=kanban__pb2.Label.FromString,
                )
        self.GetLabels = channel.unary_unary(
                '/kanban_package.KanbanPackage/GetLabels',
                request_serializer=kanban__pb2.BoardResponse.SerializeToString,
                response_deserializer=kanban__pb2.GetLabelsResponse.FromString,
                )
        self.GetLabel = channel.unary_unary(
                '/kanban_package.KanbanPackage/GetLabel',
                request_serializer=kanban__pb2.GetLabelRequest.SerializeToString,
                response_deserializer=kanban__pb2.Label.FromString,
                )
        self.AddItem = channel.unary_unary(
                '/kanban_package.KanbanPackage/AddItem',
                request_serializer=kanban__pb2.AddItemRequest.SerializeToString,
                response_deserializer=kanban__pb2.Item.FromString,
                )
        self.GetItems = channel.unary_unary(
                '/kanban_package.KanbanPackage/GetItems',
                request_serializer=kanban__pb2.GetItemRequest.SerializeToString,
                response_deserializer=kanban__pb2.GetItemResponse.FromString,
                )
        self.GetItem = channel.unary_unary(
                '/kanban_package.KanbanPackage/GetItem',
                request_serializer=kanban__pb2.DeleteReactionRequest.SerializeToString,
                response_deserializer=kanban__pb2.Item.FromString,
                )
        self.UpdateItem = channel.unary_unary(
                '/kanban_package.KanbanPackage/UpdateItem',
                request_serializer=kanban__pb2.UpdateItemRequest.SerializeToString,
                response_deserializer=kanban__pb2.Item.FromString,
                )
        self.DeleteItem = channel.unary_unary(
                '/kanban_package.KanbanPackage/DeleteItem',
                request_serializer=kanban__pb2.DeleteReactionRequest.SerializeToString,
                response_deserializer=kanban__pb2.VoidResp.FromString,
                )
        self.AddComment = channel.unary_unary(
                '/kanban_package.KanbanPackage/AddComment',
                request_serializer=kanban__pb2.CommentRequest.SerializeToString,
                response_deserializer=kanban__pb2.Comment.FromString,
                )
        self.UpdateComment = channel.unary_unary(
                '/kanban_package.KanbanPackage/UpdateComment',
                request_serializer=kanban__pb2.UpdateCommentRequest.SerializeToString,
                response_deserializer=kanban__pb2.Comment.FromString,
                )
        self.DeleteComment = channel.unary_unary(
                '/kanban_package.KanbanPackage/DeleteComment',
                request_serializer=kanban__pb2.DeleteCommentRequest.SerializeToString,
                response_deserializer=kanban__pb2.VoidResp.FromString,
                )
        self.AddReaction = channel.unary_unary(
                '/kanban_package.KanbanPackage/AddReaction',
                request_serializer=kanban__pb2.AddReactionRequest.SerializeToString,
                response_deserializer=kanban__pb2.VoidResp.FromString,
                )
        self.DeleteReaction = channel.unary_unary(
                '/kanban_package.KanbanPackage/DeleteReaction',
                request_serializer=kanban__pb2.DeleteReactionRequest.SerializeToString,
                response_deserializer=kanban__pb2.VoidResp.FromString,
                )
        self.ExportBoard = channel.unary_unary(
                '/kanban_package.KanbanPackage/ExportBoard',
                request_serializer=kanban__pb2.BoardResponse.SerializeToString,
                response_deserializer=kanban__pb2.ExportResponse.FromString,
                )


class KanbanPackageServicer(object):
    """Missing associated documentation comment in .proto file."""

    def InitializeKanban(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddLabel(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetLabels(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetLabel(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddItem(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetItems(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetItem(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateItem(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteItem(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddComment(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateComment(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteComment(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddReaction(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteReaction(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ExportBoard(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_KanbanPackageServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'InitializeKanban': grpc.unary_unary_rpc_method_handler(
                    servicer.InitializeKanban,
                    request_deserializer=kanban__pb2.CreateKanbanRequest.FromString,
                    response_serializer=kanban__pb2.BoardResponse.SerializeToString,
            ),
            'AddLabel': grpc.unary_unary_rpc_method_handler(
                    servicer.AddLabel,
                    request_deserializer=kanban__pb2.LabelRequest.FromString,
                    response_serializer=kanban__pb2.Label.SerializeToString,
            ),
            'GetLabels': grpc.unary_unary_rpc_method_handler(
                    servicer.GetLabels,
                    request_deserializer=kanban__pb2.BoardResponse.FromString,
                    response_serializer=kanban__pb2.GetLabelsResponse.SerializeToString,
            ),
            'GetLabel': grpc.unary_unary_rpc_method_handler(
                    servicer.GetLabel,
                    request_deserializer=kanban__pb2.GetLabelRequest.FromString,
                    response_serializer=kanban__pb2.Label.SerializeToString,
            ),
            'AddItem': grpc.unary_unary_rpc_method_handler(
                    servicer.AddItem,
                    request_deserializer=kanban__pb2.AddItemRequest.FromString,
                    response_serializer=kanban__pb2.Item.SerializeToString,
            ),
            'GetItems': grpc.unary_unary_rpc_method_handler(
                    servicer.GetItems,
                    request_deserializer=kanban__pb2.GetItemRequest.FromString,
                    response_serializer=kanban__pb2.GetItemResponse.SerializeToString,
            ),
            'GetItem': grpc.unary_unary_rpc_method_handler(
                    servicer.GetItem,
                    request_deserializer=kanban__pb2.DeleteReactionRequest.FromString,
                    response_serializer=kanban__pb2.Item.SerializeToString,
            ),
            'UpdateItem': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateItem,
                    request_deserializer=kanban__pb2.UpdateItemRequest.FromString,
                    response_serializer=kanban__pb2.Item.SerializeToString,
            ),
            'DeleteItem': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteItem,
                    request_deserializer=kanban__pb2.DeleteReactionRequest.FromString,
                    response_serializer=kanban__pb2.VoidResp.SerializeToString,
            ),
            'AddComment': grpc.unary_unary_rpc_method_handler(
                    servicer.AddComment,
                    request_deserializer=kanban__pb2.CommentRequest.FromString,
                    response_serializer=kanban__pb2.Comment.SerializeToString,
            ),
            'UpdateComment': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateComment,
                    request_deserializer=kanban__pb2.UpdateCommentRequest.FromString,
                    response_serializer=kanban__pb2.Comment.SerializeToString,
            ),
            'DeleteComment': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteComment,
                    request_deserializer=kanban__pb2.DeleteCommentRequest.FromString,
                    response_serializer=kanban__pb2.VoidResp.SerializeToString,
            ),
            'AddReaction': grpc.unary_unary_rpc_method_handler(
                    servicer.AddReaction,
                    request_deserializer=kanban__pb2.AddReactionRequest.FromString,
                    response_serializer=kanban__pb2.VoidResp.SerializeToString,
            ),
            'DeleteReaction': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteReaction,
                    request_deserializer=kanban__pb2.DeleteReactionRequest.FromString,
                    response_serializer=kanban__pb2.VoidResp.SerializeToString,
            ),
            'ExportBoard': grpc.unary_unary_rpc_method_handler(
                    servicer.ExportBoard,
                    request_deserializer=kanban__pb2.BoardResponse.FromString,
                    response_serializer=kanban__pb2.ExportResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'kanban_package.KanbanPackage', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class KanbanPackage(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def InitializeKanban(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/kanban_package.KanbanPackage/InitializeKanban',
            kanban__pb2.CreateKanbanRequest.SerializeToString,
            kanban__pb2.BoardResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AddLabel(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/kanban_package.KanbanPackage/AddLabel',
            kanban__pb2.LabelRequest.SerializeToString,
            kanban__pb2.Label.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetLabels(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/kanban_package.KanbanPackage/GetLabels',
            kanban__pb2.BoardResponse.SerializeToString,
            kanban__pb2.GetLabelsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetLabel(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/kanban_package.KanbanPackage/GetLabel',
            kanban__pb2.GetLabelRequest.SerializeToString,
            kanban__pb2.Label.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AddItem(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/kanban_package.KanbanPackage/AddItem',
            kanban__pb2.AddItemRequest.SerializeToString,
            kanban__pb2.Item.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetItems(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/kanban_package.KanbanPackage/GetItems',
            kanban__pb2.GetItemRequest.SerializeToString,
            kanban__pb2.GetItemResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetItem(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/kanban_package.KanbanPackage/GetItem',
            kanban__pb2.DeleteReactionRequest.SerializeToString,
            kanban__pb2.Item.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateItem(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/kanban_package.KanbanPackage/UpdateItem',
            kanban__pb2.UpdateItemRequest.SerializeToString,
            kanban__pb2.Item.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteItem(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/kanban_package.KanbanPackage/DeleteItem',
            kanban__pb2.DeleteReactionRequest.SerializeToString,
            kanban__pb2.VoidResp.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AddComment(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/kanban_package.KanbanPackage/AddComment',
            kanban__pb2.CommentRequest.SerializeToString,
            kanban__pb2.Comment.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateComment(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/kanban_package.KanbanPackage/UpdateComment',
            kanban__pb2.UpdateCommentRequest.SerializeToString,
            kanban__pb2.Comment.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteComment(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/kanban_package.KanbanPackage/DeleteComment',
            kanban__pb2.DeleteCommentRequest.SerializeToString,
            kanban__pb2.VoidResp.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AddReaction(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/kanban_package.KanbanPackage/AddReaction',
            kanban__pb2.AddReactionRequest.SerializeToString,
            kanban__pb2.VoidResp.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteReaction(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/kanban_package.KanbanPackage/DeleteReaction',
            kanban__pb2.DeleteReactionRequest.SerializeToString,
            kanban__pb2.VoidResp.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ExportBoard(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/kanban_package.KanbanPackage/ExportBoard',
            kanban__pb2.BoardResponse.SerializeToString,
            kanban__pb2.ExportResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

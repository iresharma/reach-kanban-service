import grpc
from google.protobuf.json_format import MessageToDict

from pb.kanban_pb2_grpc import KanbanPackageServicer
import pb.kanban_pb2 as models
from concurrent import futures
import pb.kanban_pb2_grpc as kanban_grpc

from parseable.logger import infoLog, ErrorLog

from database import createBoard, addLabel, addItem, getItem, updateItem, getLabel, getLabels, addComment, \
    updateComment, deleteComment, getitem, deleteItem


class Service(KanbanPackageServicer):

    def InitializeKanban(self, request: models.CreateKanbanRequest, context):
        infoLog(message="Creating new board for user account", context={"X-UserAccount": request.UserAccountId})
        user_Account = request.UserAccountId
        id = createBoard(user_Account)
        return models.BoardResponse(id=id)

    def AddLabel(self, request: models.LabelRequest, context):
        infoLog(message="Adding new label for board", context=MessageToDict(request))
        name = request.name
        color = request.color
        board_id = request.boardId
        label = addLabel(name, color, board_id)
        infoLog(message=f"Added new label {label.id} to board {request.boardId}", context=MessageToDict(request))
        return models.Label(
            id=label.id,
            name=name,
            color=color,
            boardId=board_id
        )

    def GetLabel(self, request: models.GetLabelRequest, context):
        infoLog(message=f"Getting {request.labelId} label for board", context=MessageToDict(request))
        label_id = request.labelId
        label = getLabel(label_id)
        return models.Label(
            id=str(label.id),
            name=str(label.name),
            color=str(label.color),
            boardId=str(label.boardId)
        )

    def GetLabels(self, request: models.BoardResponse, context):
        infoLog(message="Getting all labels for board", context=MessageToDict(request))
        board_id = request.id
        labels = getLabels(board_id)
        return models.GetLabelsResponse(
            labels=labels
        )

    def AddItem(self, request: models.AddItemRequest, context):
        infoLog(message=f"Add new item to board {request.boardId}", context=MessageToDict(request))
        label = request.label
        status = request.status
        title = request.title
        desc = request.desc
        links = request.links
        boardId = request.boardId
        userId = request.userId
        item = addItem(label, str(status), title, desc, str(links), boardId, userId)
        infoLog(message=f"Added new item {item.id} to board {request.boardId}", context=MessageToDict(request))
        try:
            model = models.Item(
                id=item.id,
                label=models.Label(id=label),
                status=item.status,
                title=item.title,
                desc=item.desc,
                links=item.links,
                comments=[],
                userId=userId
            )
            return model
        except Exception as e:
            ErrorLog(error=e, message="Failed parsing add item")

    def GetItems(self, request: models.GetItemRequest, context):
        infoLog(message=f"Get Items for board {request.board}", context=MessageToDict(request))
        page = request.page
        limit = request.limit
        board = request.board
        items = getItem(page, limit, board)
        return models.GetItemResponse(
            items=items,
            page=(page + 1)
        )

    def GetItem(self, request: models.DeleteCommentRequest, context):
        infoLog(message=f"Getting Item {request.id}", context=MessageToDict(request))
        id = request.id
        return getitem(id)

    def UpdateItem(self, request: models.UpdateItemRequest, context):
        infoLog(message=f"Update Item {request.id}", context=MessageToDict(request))
        updateItem(
            request.id,
            request.label,
            request.status,
            request.title,
            request.desc,
            request.links,
        )
        model = models.Item(
            id=request.id,
            label=models.Label(id=request.id),
            status=request.status,
            title=request.title,
            desc=request.desc,
            links=request.links,
        )
        return model

    def DeleteItem(self, request: models.DeleteReactionRequest, context):
        infoLog(message=f"Deleting Item {request.id}", context=MessageToDict(request))
        id = request.id
        deleteItem(id)
        return models.VoidResp()

    def AddComment(self, request: models.CommentRequest, context):
        infoLog(message=f"Adding comment to Item {request.ItemId}", context=MessageToDict(request))
        message = request.message
        user_id = request.userId
        item_id = request.ItemId
        comment = addComment(message, item_id, user_id)
        return models.Comment(
            id=comment.id,
            message=message,
            userId=user_id,
        )

    def UpdateComment(self, request: models.UpdateCommentRequest, context):
        infoLog(message=f"Updating comment {request.id}", context=MessageToDict(request))
        comment_id = request.id
        message = request.message
        updateComment(comment_id, message)
        return models.Comment(
            id=comment_id,
            message=message,
        )

    def DeleteComment(self, request: models.DeleteCommentRequest, context):
        infoLog(message=f"Deleting comment {request.id}", context=MessageToDict(request))
        comment_id = request.id
        deleteComment(comment_id)
        return models.VoidResp()


    def AddReaction(self, request, context):
        pass

    def DeleteReaction(self, request, context):
        pass

    def ExportBoard(self, request: models.BoardResponse, context):
        return models.ExportResponse(downloadLink="Feature not implemented")


if __name__ == "__main__":
    port = "4040"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    kanban_grpc.add_KanbanPackageServicer_to_server(Service(), server)
    server.add_insecure_port("[::]:" + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()

import grpc

from pb.kanban_pb2_grpc import KanbanPackageServicer
import pb.kanban_pb2 as models
from concurrent import futures
import pb.kanban_pb2_grpc as kanban_grpc

from database import createBoard, addLabel, addItem, getItem, updateItem


class Service(KanbanPackageServicer):

    def InitializeKanban(self, request: models.CreateKanbanRequest, context):
        user_Account = request.UserAccountId
        id = createBoard(user_Account)
        return models.BoardResponse(id=id)

    def AddLabel(self, request: models.LabelRequest, context):
        name = request.name
        color = request.color
        board_id = request.boardId
        label = addLabel(name, color, board_id)
        return models.Label(
            id=label.id,
            name=name,
            color=color,
            boardId=board_id
        )

    def AddItem(self, request: models.AddItemRequest, context):
        label = request.label
        status = request.status
        title = request.title
        desc = request.desc
        links = request.links
        boardId = request.boardId
        userId = request.userId
        item = addItem(label, str(status), title, desc, str(links), boardId, userId)
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
            print(e)

    def GetItems(self, request: models.GetItemRequest, context):
        page = request.page
        limit = request.limit
        board = request.board
        items = getItem(page, limit, board)
        print(items)
        return models.GetItemResponse(
            items=items,
            page=(page + 1)
        )

    def UpdateItem(self, request: models.UpdateItemRequest, context):
        print(request.id)
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

    def AddComment(self, request: models.CommentRequest, context):
        pass

    def UpdateComment(self, request, context):
        pass

    def DeleteComment(self, request, context):
        pass

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

import grpc

from pb.kanban_pb2_grpc import KanbanPackageServicer
import pb.kanban_pb2 as models
from concurrent import futures
import pb.kanban_pb2_grpc as kanban_grpc

from database import createBoard, addLabel, addItem, getItem


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
        item = addItem(label, str(status), title, desc, str(links), boardId)
        try:
            model = models.Item(
                id=item.id,
                # label=item.label,
                status=item.status,
                title=item.title,
                desc=item.desc,
                links=item.links,
                comments=[]
            )
            return model
        except Exception as e:
            print(e)

    def GetItems(self, request: models.GetItemRequest, context):
        page = request.page
        limit = request.limit
        board = request.board
        items = getItem(page, limit, board)
        return models.GetItemResponse(
            items=items,
            page=(page + 1)
        )


    def UpdateItem(self, request, context):
        pass

    def UpdateStatus(self, request, context):
        pass


if __name__ == "__main__":
    port = "4040"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    kanban_grpc.add_KanbanPackageServicer_to_server(Service(), server)
    server.add_insecure_port("[::]:" + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()

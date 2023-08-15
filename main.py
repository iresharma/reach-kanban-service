import grpc

from pb.kanban_pb2_grpc import KanbanPackageServicer
import pb.kanban_pb2 as models
from concurrent import futures
import pb.kanban_pb2_grpc as kanban_grpc

from database import createBoard, addLabel

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

    def AddItem(self, request, context):
        pass

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

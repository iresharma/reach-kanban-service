import grpc

from pb.kanban_pb2_grpc import KanbanPackageServicer
import pb.kanban_pb2 as models
from uuid import uuid4
from concurrent import futures
import pb.kanban_pb2_grpc as kanban_grpc

class Service(KanbanPackageServicer):

    def InitializeKanban(self, request: models.CreateKanbanRequest, context):
        user_Account = request.UserAccountId
        print("heelo")
        return models.BoardResponse(id=str(uuid4()))

    def GetKanban(self, request, context):
        pass

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

from pb.kanban_pb2_grpc import KanbanPackageServicer
import pb.kanban_pb2 as models

class Service(KanbanPackageServicer):

    def InitializeKanban(self, request: models.CreateKanbanRequest, context):
        userAccount = request.UserAccountId


    def GetKanban(self, request, context):
        pass

    def AddItem(self, request, context):
        pass

    def UpdateItem(self, request, context):
        pass

    def UpdateStatus(self, request, context):
        pass
from pony.orm import *
import pb.kanban_pb2 as models
from enum import Enum
from uuid import uuid4

db = Database()
db.bind(provider='postgres', user='iresharma', password='DjP5OMamofu9',
        host='ep-yellow-hill-73697354.ap-southeast-1.aws.neon.tech', database='neondb')


class UserAccount(db.Entity):
    id = Required(str)
    account_name = Required(str)
    email = Required(str)
    created_at = Required(int)
    photo_url = Required(str)
    users = Set(str)
    owner = Required(str)
    pageId = Required(str)
    bucketId = Required(str)
    boardId = Required(str)

    def to_proto(self):
        return models.UserAccount(
            id=self.id,
            account_name=self.account_name,
            email=self.email,
            created_at=self.created_at,
            photo_url=self.photo_url,
            users=self.users,
            owner=self.owner,
            pageId=self.pageId,
            bucketId=self.bucketId,
            boardId=self.boardId
        )


class Board(db.Entity):
    id = Required(str)
    items = Set('Item')
    user_account = Required(UserAccount)


class Item(db.Entity):
    id = Required(str)
    title = Required(str)
    desc = Required(str)
    priority = Enum('Priority', ['LOW', 'MED', 'HIGH'])
    script = str
    reference = str
    storage = str
    prefix = str
    board = Required(Board)

    def to_proto(self):
        return models.Item(
            self.id,
            self.title,
            self.desc,
            self.priority.value,
            self.script,
            self.reference,
            self.storage,
            self.board.id
        )


@db_session
def initKanban(userAccountId: str):
    board = Board(
        id=str(uuid4()),
        items=[],
        user_account=userAccountId
    )
    user_account = UserAccount.get(id=userAccountId)
    user_account.get_for_update()


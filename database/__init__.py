from peewee import PostgresqlDatabase, Model, CharField, ForeignKeyField
from os import environ
from uuid import uuid4

db = PostgresqlDatabase(environ['DB_NAME'], user=environ['DB_USER'], password=environ['DB_PASSWORD'],
                        host=environ['DB_HOST'], port=environ["DB_PORT"])


class BaseModel(Model):
    class Meta:
        database = db


class Board(BaseModel):
    id = CharField(primary_key=True)


class KanbanLabel(BaseModel):
    id = CharField(primary_key=True)
    name = CharField(unique=True)
    color = CharField()
    boardId = ForeignKeyField(Board, backref="labels")


class Item(BaseModel):
    id = CharField(primary_key=True)
    label = KanbanLabel
    status = CharField()
    title = CharField()
    desc = CharField()
    links = CharField()
    board = ForeignKeyField(Board, backref="items")


class Comment(BaseModel):
    id = CharField(primary_key=True)
    userId = CharField()
    message = CharField()
    item = ForeignKeyField(Item, backref="comments")


with db:
    db.create_tables([Board, Item, KanbanLabel, Comment])


def createBoard(user_Account: str) -> str:
    try:
        with db.atomic():
            board = Board.create(
                id=str(uuid4()),
            )
            db.execute_sql("update user_accounts set board_id = '{}' where id = '{}' and user_accounts.board_id is not null".format(board.id, user_Account))
        return board.id
    except Exception as e:
        print(e)


def addLabel(name: str, color: str, board_id: str) -> KanbanLabel:
    print(name, color, board_id)
    try:
        with db.atomic():
            label = KanbanLabel.create(
                id=str(uuid4()),
                name=name,
                color=color,
                boardId=board_id
            )
        return label
    except Exception as e:
        print(e)

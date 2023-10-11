from peewee import PostgresqlDatabase, Model, CharField, ForeignKeyField, JOIN
from os import environ
from uuid import uuid4
from pb.kanban_pb2 import Item as RPCItem, Label, STATUS

db = PostgresqlDatabase(environ['DB_NAME'], user=environ['DB_USER'], password=environ['DB_PASSWORD'],
                        host=environ['DB_HOST'], port=environ["DB_PORT"])

status = {
    "0": "TODO",
    "1": "PROGRESS",
    "2": "COMPLETED",
    "3": "CANCELED",
    "4": "BACKLOG",
    "TODO": "TODO",
    "PROGRESS": "PROGRESS",
    "COMPLETED": "COMPLETED",
    "CANCELED": "CANCELED",
    "BACKLOG": "BACKLOG",
}


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
    status = CharField()
    title = CharField()
    desc = CharField()
    links = CharField()
    board = ForeignKeyField(Board, backref="items")
    label = ForeignKeyField(KanbanLabel, backref="item")
    userId = CharField()


class Comment(BaseModel):
    id = CharField(primary_key=True)
    userId = CharField()
    message = CharField()
    item = ForeignKeyField(Item, backref="comments")


class Reaction(BaseModel):
    id = CharField(primary_key=True)
    userId = CharField()
    emoji = CharField()


with db:
    db.create_tables([Board, Item, KanbanLabel, Comment])


def createBoard(user_Account: str) -> str:
    try:
        with db.atomic():
            board = Board.create(
                id=str(uuid4()),
            )
            db.execute_sql(
                "update user_accounts set board_id = '{}' where id = '{}' and user_accounts.board_id is not null".format(
                    board.id, user_Account))
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


def addItem(label: str, status: str, title: str, desc: str, links: str, board_id: str, user_id: str) -> Item:
    try:
        with db.atomic():
            status_list = [
                "TODO",
                "PROGRESS",
                "COMPLETED",
                "CANCELED",
                "BACKLOG",
            ]
            item = Item.create(
                id="TASK-" + str(uuid4()).split("-").pop(),
                label=label,
                status=status_list[int(status)],
                title=title,
                desc=desc,
                links=links,
                board=board_id,
                userId=user_id
            )
            return item
    except Exception as e:
        print(e)


def ItemToRPCItem(item: dict) -> RPCItem:
    return RPCItem(
        id=item["id"],
        label=Label(
            id=item["label"],
            name=item["name"],
            color=item["color"]
        ),
        status=status[item["status"]],
        title=item["title"],
        desc=item["desc"],
        links=item["links"],
        userId=""
    )


def getItem(page: int, limit: int, board_id: str) -> list:
    try:
        with db.atomic():
            keys = [
                Item.id,
                Item.status,
                Item.title,
                Item.desc,
                Item.links,
                Item.label,
                KanbanLabel.color,
                KanbanLabel.name
            ]
            items = Item.select(*keys).join(KanbanLabel).offset(page * limit).limit(limit).where(
                Item.board == board_id).dicts()
            print(list(items))
            return list(map(ItemToRPCItem, items))
    except Exception as e:
        print(e)


def updateItem(item_id: str, label: str, input_status: STATUS, title: str, desc: str, links: str):
    try:
        with db.atomic():
            row = Item.update(
                label=label,
                status=status[str(input_status)],
                title=title,
                desc=desc,
                links=links
            ).where(Item.id == item_id)
            row.execute()
    except Exception as e:
        print(type(e))

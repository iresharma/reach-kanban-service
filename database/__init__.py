from peewee import PostgresqlDatabase, Model, CharField, ForeignKeyField, JOIN, TextField
from os import environ
from uuid import uuid4

from parseable.logger import ErrorLog
from pb.kanban_pb2 import Item as RPCItem, Label, STATUS, Comment as RPCComment
from playhouse.db_url import connect

db = connect(environ.get('POSTGRES'))

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
    name = CharField()
    color = CharField()
    boardId = ForeignKeyField(Board, backref="labels")


class Item(BaseModel):
    id = CharField(primary_key=True)
    status = CharField()
    title = CharField()
    desc = TextField()
    links = CharField()
    board = ForeignKeyField(Board, backref="items")
    label = ForeignKeyField(KanbanLabel, backref="item")
    userId = CharField()


class Comment(BaseModel):
    id = CharField(primary_key=True)
    userId = CharField()
    message = TextField()
    item = ForeignKeyField(Item, backref="comments")


class Reaction(BaseModel):
    id = CharField(primary_key=True)
    userId = CharField()
    emoji = CharField()
    comment = ForeignKeyField(Comment, backref="reactions")


with db:
    db.create_tables([Board, Item, KanbanLabel, Comment, Reaction])


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
        ErrorLog(error=e, context={"X-UserAccount": user_Account})


def addLabel(name: str, color: str, board_id: str) -> KanbanLabel:
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
        ErrorLog(error=e, board=board_id, message="Could not add label")


def getLabels(board_id: str):
    try:
        with db.atomic():
            keys = [
                KanbanLabel.id,
                KanbanLabel.color,
                KanbanLabel.name
            ]
            labels = KanbanLabel.select(*keys).where(KanbanLabel.boardId == board_id).dicts()
            return list(labels)
    except Exception as e:
        ErrorLog(error=e, board=board_id, message="Could not get any labels")


def getLabel(label_id: str) -> Label:
    try:
        with db.atomic():
            label = KanbanLabel.get_by_id(label_id)
            return label
    except Exception as e:
        ErrorLog(error=e, message="Could not find label")

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
        ErrorLog(error=e, message="failed while adding item", board=board_id)


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
        userId="",
        comments=list(map(lambda x: RPCComment(
            id=x["id"],
            message=x["message"],
            userId=x["userId"],
            reactions=[]
        ), item["comments"]))
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
            for item in items:
                comments = Comment.select().where(Comment.item == item["id"]).dicts()
                item["comments"] = comments
            return list(map(ItemToRPCItem, items))
    except Exception as e:
        ErrorLog(error=e, message="failed while getting items", board=board_id)
        print(e)


def getitem(id: str):
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
            item = Item.select(*keys).join(KanbanLabel).where(Item.id == id).dicts()
            comments = Comment.select().where(Comment.item == id).dicts()
            item[0]["comments"] = comments
            return ItemToRPCItem(item[0])
    except Exception as e:
        ErrorLog(error=e, message=f"failed while getting item {id}")
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
        ErrorLog(error=e, message=f"failed while updating item {item_id}")
        print(type(e))


def deleteItem(item_id: str):
    try:
        with db.atomic():
            print(item_id)
            db.execute_sql("DELETE FROM Item WHERE Item.id = {}".format(item_id))
    except Exception as e:
        ErrorLog(error=e, message=f"failed while deleting item {item_id}")
        print(e)


def addComment(message: str, item_id: str, user_id: str) -> Comment:
    try:
        with db.atomic():
            comment = Comment.create(
                id=str(uuid4()),
                message=message,
                item_id=item_id,
                userId=user_id
            )
            return comment
    except Exception as e:
        ErrorLog(error=e, message=f"failed while adding comment item {item_id}")
        print(e)


def updateComment(comment_id: str, message: str):
    try:
        with db.atomic():
            row = Comment.update(
                message=message,
            ).where(Comment.id == comment_id)
            row.execute()
    except Exception as e:
        ErrorLog(error=e, message=f"failed while updating comment {comment_id}")
        print(e)


def deleteComment(comment_id: str):
    try:
        with db.atomic():
            Comment.delete().where(Comment.id == comment_id).execute()
    except Exception as e:
        ErrorLog(error=e, message=f"failed while deleting comment {comment_id}")
        print(e)

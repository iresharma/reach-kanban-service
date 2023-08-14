# import uuid
#
# from pony.orm import *
# from os import environ
#
# db = Database()
# db.bind(provider='postgres', user=environ['DB_USER'], password=environ['DB_PASSWORD'], host=environ['DB_HOST'],
#         database=environ['DB_NAME'], sslmode="require", sslrootcert="../root.crt")
#
#
# class Board(db.Entity):
#     id = Required(str)
#     labels = Set("Label")
#     items = Set("Item")
#
#
# class UserAccount(db.Entity):
#     id = Required(str)
#     account_name = Required(str)
#     email = Required(str)
#     photo_url = str
#     users = Required(StrArray)
#     owner = Required(str)
#     pageId = str
#     bucketId = str
#     boardId = Optional(Board)
#
#
# class KanbanLabel(db.Entity):
#     id = Required(str)
#     name = Required(str)
#     color = Required(str)
#     boardId = Required(Board)
#
#
# class Comment(db.Entity):
#     id = Required(str)
#     userId = Required(str)
#     message = Required(str)
#
#
# class Item(db.Entity):
#     id = Required(str)
#     label = Required(KanbanLabel)
#     status = Required(str)
#     title = Required(str)
#     desc = str
#     links = Optional(dict)
#     comment = Set(Comment)
#     board = Board
#
#
# db.generate_mapping(create_tables=False)
# db.create_tables(KanbanLabel, Comment, Item)
#
#
# def InitKanban(user_account: str) -> Board:
#     board = Board(
#         id=str(uuid.uuid4()),
#         labels=[],
#         items=[]
#     )
#     commit()
#     return board

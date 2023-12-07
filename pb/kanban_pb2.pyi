from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class STATUS(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    TODO: _ClassVar[STATUS]
    PROGRESS: _ClassVar[STATUS]
    COMPLETED: _ClassVar[STATUS]
    CANCELED: _ClassVar[STATUS]
    BACKLOG: _ClassVar[STATUS]
TODO: STATUS
PROGRESS: STATUS
COMPLETED: STATUS
CANCELED: STATUS
BACKLOG: STATUS

class UserAccount(_message.Message):
    __slots__ = ["id", "account_name", "email", "created_at", "photo_url", "users", "owner", "pageId", "bucketId", "boardId"]
    ID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_NAME_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    PHOTO_URL_FIELD_NUMBER: _ClassVar[int]
    USERS_FIELD_NUMBER: _ClassVar[int]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    PAGEID_FIELD_NUMBER: _ClassVar[int]
    BUCKETID_FIELD_NUMBER: _ClassVar[int]
    BOARDID_FIELD_NUMBER: _ClassVar[int]
    id: str
    account_name: str
    email: str
    created_at: _timestamp_pb2.Timestamp
    photo_url: str
    users: _containers.RepeatedScalarFieldContainer[str]
    owner: str
    pageId: str
    bucketId: str
    boardId: str
    def __init__(self, id: _Optional[str] = ..., account_name: _Optional[str] = ..., email: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., photo_url: _Optional[str] = ..., users: _Optional[_Iterable[str]] = ..., owner: _Optional[str] = ..., pageId: _Optional[str] = ..., bucketId: _Optional[str] = ..., boardId: _Optional[str] = ...) -> None: ...

class Label(_message.Message):
    __slots__ = ["id", "name", "color", "boardId"]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    BOARDID_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    color: str
    boardId: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., color: _Optional[str] = ..., boardId: _Optional[str] = ...) -> None: ...

class Comment(_message.Message):
    __slots__ = ["id", "userId", "message", "reactions"]
    ID_FIELD_NUMBER: _ClassVar[int]
    USERID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    REACTIONS_FIELD_NUMBER: _ClassVar[int]
    id: str
    userId: str
    message: str
    reactions: _containers.RepeatedCompositeFieldContainer[Reaction]
    def __init__(self, id: _Optional[str] = ..., userId: _Optional[str] = ..., message: _Optional[str] = ..., reactions: _Optional[_Iterable[_Union[Reaction, _Mapping]]] = ...) -> None: ...

class Reaction(_message.Message):
    __slots__ = ["id", "userId", "emoji"]
    ID_FIELD_NUMBER: _ClassVar[int]
    USERID_FIELD_NUMBER: _ClassVar[int]
    EMOJI_FIELD_NUMBER: _ClassVar[int]
    id: str
    userId: str
    emoji: str
    def __init__(self, id: _Optional[str] = ..., userId: _Optional[str] = ..., emoji: _Optional[str] = ...) -> None: ...

class Item(_message.Message):
    __slots__ = ["id", "label", "status", "title", "desc", "links", "comments", "userId"]
    ID_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    DESC_FIELD_NUMBER: _ClassVar[int]
    LINKS_FIELD_NUMBER: _ClassVar[int]
    COMMENTS_FIELD_NUMBER: _ClassVar[int]
    USERID_FIELD_NUMBER: _ClassVar[int]
    id: str
    label: Label
    status: STATUS
    title: str
    desc: str
    links: str
    comments: _containers.RepeatedCompositeFieldContainer[Comment]
    userId: str
    def __init__(self, id: _Optional[str] = ..., label: _Optional[_Union[Label, _Mapping]] = ..., status: _Optional[_Union[STATUS, str]] = ..., title: _Optional[str] = ..., desc: _Optional[str] = ..., links: _Optional[str] = ..., comments: _Optional[_Iterable[_Union[Comment, _Mapping]]] = ..., userId: _Optional[str] = ...) -> None: ...

class Board(_message.Message):
    __slots__ = ["id", "items", "labels"]
    ID_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    id: str
    items: _containers.RepeatedCompositeFieldContainer[Item]
    labels: _containers.RepeatedCompositeFieldContainer[Label]
    def __init__(self, id: _Optional[str] = ..., items: _Optional[_Iterable[_Union[Item, _Mapping]]] = ..., labels: _Optional[_Iterable[_Union[Label, _Mapping]]] = ...) -> None: ...

class CreateKanbanRequest(_message.Message):
    __slots__ = ["UserAccountId"]
    USERACCOUNTID_FIELD_NUMBER: _ClassVar[int]
    UserAccountId: str
    def __init__(self, UserAccountId: _Optional[str] = ...) -> None: ...

class LabelRequest(_message.Message):
    __slots__ = ["name", "color", "boardId"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    BOARDID_FIELD_NUMBER: _ClassVar[int]
    name: str
    color: str
    boardId: str
    def __init__(self, name: _Optional[str] = ..., color: _Optional[str] = ..., boardId: _Optional[str] = ...) -> None: ...

class AddItemRequest(_message.Message):
    __slots__ = ["label", "status", "title", "desc", "links", "boardId", "userId"]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    DESC_FIELD_NUMBER: _ClassVar[int]
    LINKS_FIELD_NUMBER: _ClassVar[int]
    BOARDID_FIELD_NUMBER: _ClassVar[int]
    USERID_FIELD_NUMBER: _ClassVar[int]
    label: str
    status: STATUS
    title: str
    desc: str
    links: str
    boardId: str
    userId: str
    def __init__(self, label: _Optional[str] = ..., status: _Optional[_Union[STATUS, str]] = ..., title: _Optional[str] = ..., desc: _Optional[str] = ..., links: _Optional[str] = ..., boardId: _Optional[str] = ..., userId: _Optional[str] = ...) -> None: ...

class BoardResponse(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetItemRequest(_message.Message):
    __slots__ = ["page", "limit", "board"]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    BOARD_FIELD_NUMBER: _ClassVar[int]
    page: int
    limit: int
    board: str
    def __init__(self, page: _Optional[int] = ..., limit: _Optional[int] = ..., board: _Optional[str] = ...) -> None: ...

class GetItemResponse(_message.Message):
    __slots__ = ["items", "page"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[Item]
    page: int
    def __init__(self, items: _Optional[_Iterable[_Union[Item, _Mapping]]] = ..., page: _Optional[int] = ...) -> None: ...

class ExportResponse(_message.Message):
    __slots__ = ["downloadLink"]
    DOWNLOADLINK_FIELD_NUMBER: _ClassVar[int]
    downloadLink: str
    def __init__(self, downloadLink: _Optional[str] = ...) -> None: ...

class UpdateItemRequest(_message.Message):
    __slots__ = ["id", "label", "status", "title", "desc", "links"]
    ID_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    DESC_FIELD_NUMBER: _ClassVar[int]
    LINKS_FIELD_NUMBER: _ClassVar[int]
    id: str
    label: str
    status: STATUS
    title: str
    desc: str
    links: str
    def __init__(self, id: _Optional[str] = ..., label: _Optional[str] = ..., status: _Optional[_Union[STATUS, str]] = ..., title: _Optional[str] = ..., desc: _Optional[str] = ..., links: _Optional[str] = ...) -> None: ...

class CommentRequest(_message.Message):
    __slots__ = ["ItemId", "message", "userId"]
    ITEMID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    USERID_FIELD_NUMBER: _ClassVar[int]
    ItemId: str
    message: str
    userId: str
    def __init__(self, ItemId: _Optional[str] = ..., message: _Optional[str] = ..., userId: _Optional[str] = ...) -> None: ...

class UpdateCommentRequest(_message.Message):
    __slots__ = ["id", "message"]
    ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    id: str
    message: str
    def __init__(self, id: _Optional[str] = ..., message: _Optional[str] = ...) -> None: ...

class DeleteCommentRequest(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class AddReactionRequest(_message.Message):
    __slots__ = ["userId", "commentId", "emoji"]
    USERID_FIELD_NUMBER: _ClassVar[int]
    COMMENTID_FIELD_NUMBER: _ClassVar[int]
    EMOJI_FIELD_NUMBER: _ClassVar[int]
    userId: str
    commentId: str
    emoji: str
    def __init__(self, userId: _Optional[str] = ..., commentId: _Optional[str] = ..., emoji: _Optional[str] = ...) -> None: ...

class DeleteReactionRequest(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetLabelsResponse(_message.Message):
    __slots__ = ["labels"]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    labels: _containers.RepeatedCompositeFieldContainer[Label]
    def __init__(self, labels: _Optional[_Iterable[_Union[Label, _Mapping]]] = ...) -> None: ...

class GetLabelRequest(_message.Message):
    __slots__ = ["labelId"]
    LABELID_FIELD_NUMBER: _ClassVar[int]
    labelId: str
    def __init__(self, labelId: _Optional[str] = ...) -> None: ...

class VoidResp(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

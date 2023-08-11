from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateKanbanRequest(_message.Message):
    __slots__ = ["UserAccountId"]
    USERACCOUNTID_FIELD_NUMBER: _ClassVar[int]
    UserAccountId: str
    def __init__(self, UserAccountId: _Optional[str] = ...) -> None: ...

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

class GetKanbanRequest(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class Item(_message.Message):
    __slots__ = ["id", "title", "description", "priority", "script", "reference", "storage", "status", "created_at", "boardId"]
    class PRIORITY(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
        LOW: _ClassVar[Item.PRIORITY]
        MED: _ClassVar[Item.PRIORITY]
        HIGH: _ClassVar[Item.PRIORITY]
    LOW: Item.PRIORITY
    MED: Item.PRIORITY
    HIGH: Item.PRIORITY
    ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_FIELD_NUMBER: _ClassVar[int]
    SCRIPT_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_FIELD_NUMBER: _ClassVar[int]
    STORAGE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    BOARDID_FIELD_NUMBER: _ClassVar[int]
    id: str
    title: str
    description: str
    priority: Item.PRIORITY
    script: str
    reference: str
    storage: str
    status: str
    created_at: _timestamp_pb2.Timestamp
    boardId: str
    def __init__(self, id: _Optional[str] = ..., title: _Optional[str] = ..., description: _Optional[str] = ..., priority: _Optional[_Union[Item.PRIORITY, str]] = ..., script: _Optional[str] = ..., reference: _Optional[str] = ..., storage: _Optional[str] = ..., status: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., boardId: _Optional[str] = ...) -> None: ...

class KanbanResponse(_message.Message):
    __slots__ = ["id", "items", "userAccountId"]
    ID_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    USERACCOUNTID_FIELD_NUMBER: _ClassVar[int]
    id: str
    items: _containers.RepeatedCompositeFieldContainer[Item]
    userAccountId: str
    def __init__(self, id: _Optional[str] = ..., items: _Optional[_Iterable[_Union[Item, _Mapping]]] = ..., userAccountId: _Optional[str] = ...) -> None: ...

class UpdateStatusRequest(_message.Message):
    __slots__ = ["id", "status"]
    ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    id: str
    status: str
    def __init__(self, id: _Optional[str] = ..., status: _Optional[str] = ...) -> None: ...

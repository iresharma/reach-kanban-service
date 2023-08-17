# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: kanban.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0ckanban.proto\x12\x0ekanban_package\x1a\x1fgoogle/protobuf/timestamp.proto\"\x85\x02\n\x0bUserAccount\x12\n\n\x02id\x18\x01 \x01(\t\x12\x14\n\x0c\x61\x63\x63ount_name\x18\x02 \x01(\t\x12\r\n\x05\x65mail\x18\x03 \x01(\t\x12.\n\ncreated_at\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x11\n\tphoto_url\x18\x05 \x01(\t\x12\r\n\x05users\x18\x06 \x03(\t\x12\r\n\x05owner\x18\x07 \x01(\t\x12\x13\n\x06pageId\x18\x08 \x01(\tH\x00\x88\x01\x01\x12\x15\n\x08\x62ucketId\x18\t \x01(\tH\x01\x88\x01\x01\x12\x14\n\x07\x62oardId\x18\n \x01(\tH\x02\x88\x01\x01\x42\t\n\x07_pageIdB\x0b\n\t_bucketIdB\n\n\x08_boardId\"A\n\x05Label\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\r\n\x05\x63olor\x18\x03 \x01(\t\x12\x0f\n\x07\x62oardId\x18\x04 \x01(\t\"6\n\x07\x43omment\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0e\n\x06userId\x18\x02 \x01(\t\x12\x0f\n\x07message\x18\x03 \x01(\t\"\xb7\x01\n\x04Item\x12\n\n\x02id\x18\x01 \x01(\t\x12$\n\x05label\x18\x02 \x01(\x0b\x32\x15.kanban_package.Label\x12&\n\x06status\x18\x03 \x01(\x0e\x32\x16.kanban_package.STATUS\x12\r\n\x05title\x18\x04 \x01(\t\x12\x0c\n\x04\x64\x65sc\x18\x05 \x01(\t\x12\r\n\x05links\x18\x06 \x01(\t\x12)\n\x08\x63omments\x18\x07 \x03(\x0b\x32\x17.kanban_package.Comment\"_\n\x05\x42oard\x12\n\n\x02id\x18\x01 \x01(\t\x12#\n\x05items\x18\x02 \x03(\x0b\x32\x14.kanban_package.Item\x12%\n\x06labels\x18\x03 \x03(\x0b\x32\x15.kanban_package.Label\",\n\x13\x43reateKanbanRequest\x12\x15\n\rUserAccountId\x18\x01 \x01(\t\"<\n\x0cLabelRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05\x63olor\x18\x02 \x01(\t\x12\x0f\n\x07\x62oardId\x18\x03 \x01(\t\"\xdd\x01\n\x0e\x41\x64\x64ItemRequest\x12\r\n\x05label\x18\x01 \x01(\t\x12&\n\x06status\x18\x02 \x01(\x0e\x32\x16.kanban_package.STATUS\x12\r\n\x05title\x18\x03 \x01(\t\x12\x0c\n\x04\x64\x65sc\x18\x04 \x01(\t\x12\x38\n\x05links\x18\x05 \x03(\x0b\x32).kanban_package.AddItemRequest.LinksEntry\x12\x0f\n\x07\x62oardId\x18\x06 \x01(\t\x1a,\n\nLinksEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x1b\n\rBoardResponse\x12\n\n\x02id\x18\x01 \x01(\t\"<\n\x0eGetItemRequest\x12\x0c\n\x04page\x18\x01 \x01(\r\x12\r\n\x05limit\x18\x02 \x01(\r\x12\r\n\x05\x62oard\x18\x03 \x01(\t\"D\n\x0fGetItemResponse\x12#\n\x05items\x18\x01 \x03(\x0b\x32\x14.kanban_package.Item\x12\x0c\n\x04page\x18\x02 \x01(\r\"&\n\x0e\x45xportResponse\x12\x14\n\x0c\x64ownloadLink\x18\x01 \x01(\t\"\xbe\x01\n\x11UpdateItemRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x12\n\x05label\x18\x02 \x01(\tH\x00\x88\x01\x01\x12+\n\x06status\x18\x03 \x01(\x0e\x32\x16.kanban_package.STATUSH\x01\x88\x01\x01\x12\x12\n\x05title\x18\x04 \x01(\tH\x02\x88\x01\x01\x12\x11\n\x04\x64\x65sc\x18\x05 \x01(\tH\x03\x88\x01\x01\x12\r\n\x05links\x18\x06 \x01(\tB\x08\n\x06_labelB\t\n\x07_statusB\x08\n\x06_titleB\x07\n\x05_desc*J\n\x06STATUS\x12\x08\n\x04TODO\x10\x00\x12\x0c\n\x08PROGRESS\x10\x01\x12\r\n\tCOMPLETED\x10\x02\x12\x0c\n\x08\x43\x41NCELED\x10\x03\x12\x0b\n\x07\x42\x41\x43KLOG\x10\x04\x32\xcb\x03\n\rKanbanPackage\x12V\n\x10InitializeKanban\x12#.kanban_package.CreateKanbanRequest\x1a\x1d.kanban_package.BoardResponse\x12?\n\x08\x41\x64\x64Label\x12\x1c.kanban_package.LabelRequest\x1a\x15.kanban_package.Label\x12?\n\x07\x41\x64\x64Item\x12\x1e.kanban_package.AddItemRequest\x1a\x14.kanban_package.Item\x12K\n\x08GetItems\x12\x1e.kanban_package.GetItemRequest\x1a\x1f.kanban_package.GetItemResponse\x12\x45\n\nUpdateItem\x12!.kanban_package.UpdateItemRequest\x1a\x14.kanban_package.Item\x12L\n\x0b\x45xportBoard\x12\x1d.kanban_package.BoardResponse\x1a\x1e.kanban_package.ExportResponseB\tZ\x07./protob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'kanban_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z\007./proto'
  _ADDITEMREQUEST_LINKSENTRY._options = None
  _ADDITEMREQUEST_LINKSENTRY._serialized_options = b'8\001'
  _globals['_STATUS']._serialized_start=1461
  _globals['_STATUS']._serialized_end=1535
  _globals['_USERACCOUNT']._serialized_start=66
  _globals['_USERACCOUNT']._serialized_end=327
  _globals['_LABEL']._serialized_start=329
  _globals['_LABEL']._serialized_end=394
  _globals['_COMMENT']._serialized_start=396
  _globals['_COMMENT']._serialized_end=450
  _globals['_ITEM']._serialized_start=453
  _globals['_ITEM']._serialized_end=636
  _globals['_BOARD']._serialized_start=638
  _globals['_BOARD']._serialized_end=733
  _globals['_CREATEKANBANREQUEST']._serialized_start=735
  _globals['_CREATEKANBANREQUEST']._serialized_end=779
  _globals['_LABELREQUEST']._serialized_start=781
  _globals['_LABELREQUEST']._serialized_end=841
  _globals['_ADDITEMREQUEST']._serialized_start=844
  _globals['_ADDITEMREQUEST']._serialized_end=1065
  _globals['_ADDITEMREQUEST_LINKSENTRY']._serialized_start=1021
  _globals['_ADDITEMREQUEST_LINKSENTRY']._serialized_end=1065
  _globals['_BOARDRESPONSE']._serialized_start=1067
  _globals['_BOARDRESPONSE']._serialized_end=1094
  _globals['_GETITEMREQUEST']._serialized_start=1096
  _globals['_GETITEMREQUEST']._serialized_end=1156
  _globals['_GETITEMRESPONSE']._serialized_start=1158
  _globals['_GETITEMRESPONSE']._serialized_end=1226
  _globals['_EXPORTRESPONSE']._serialized_start=1228
  _globals['_EXPORTRESPONSE']._serialized_end=1266
  _globals['_UPDATEITEMREQUEST']._serialized_start=1269
  _globals['_UPDATEITEMREQUEST']._serialized_end=1459
  _globals['_KANBANPACKAGE']._serialized_start=1538
  _globals['_KANBANPACKAGE']._serialized_end=1997
# @@protoc_insertion_point(module_scope)

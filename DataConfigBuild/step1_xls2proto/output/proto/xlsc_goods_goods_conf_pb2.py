# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: output/proto/xlsc_goods_goods_conf.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='output/proto/xlsc_goods_goods_conf.proto',
  package='xlsc.goods',
  serialized_pb=_b('\n(output/proto/xlsc_goods_goods_conf.proto\x12\nxlsc.goods\"\x90\x04\n\nGOODS_CONF\x12\n\n\x02id\x18\x01 \x02(\r\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x12\n\nshort_name\x18\x03 \x01(\t\x12\x36\n\x04Test\x18\x04 \x03(\x0b\x32(.xlsc.goods.GOODS_CONF.InternalType_Test\x12\x10\n\x08resource\x18\x05 \x01(\r\x12\x0c\n\x04type\x18\x06 \x01(\r\x12\x17\n\x0fup_shelves_time\x18\x07 \x01(\r\x12\x18\n\x10off_shelves_time\x18\x08 \x01(\r\x12\x12\n\nsex_detail\x18\t \x01(\x05\x12\x18\n\ris_time_limit\x18\n \x01(\x05:\x01\x30\x12\x15\n\rsmallIconType\x18\x0b \x01(\r\x12\x15\n\rsmallIconName\x18\x0c \x01(\t\x1a\xec\x01\n\x11InternalType_Test\x12\x14\n\tis_plural\x18\x01 \x01(\r:\x01\x30\x12L\n\x06Testdd\x18\x02 \x03(\x0b\x32<.xlsc.goods.GOODS_CONF.InternalType_Test.InternalType_Testdd\x12\x0c\n\x04\x64\x65sc\x18\x03 \x01(\t\x12\x10\n\x05\x63olor\x18\x04 \x01(\r:\x01\x30\x12\x11\n\tdesc_list\x18\x05 \x03(\r\x1a@\n\x13InternalType_Testdd\x12\x19\n\x0emax_plural_num\x18\x01 \x01(\r:\x01\x30\x12\x0e\n\x06rarity\x18\x02 \x01(\r\"9\n\x10GOODS_CONF_ARRAY\x12%\n\x05items\x18\x01 \x03(\x0b\x32\x16.xlsc.goods.GOODS_CONF')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_GOODS_CONF_INTERNALTYPE_TEST_INTERNALTYPE_TESTDD = _descriptor.Descriptor(
  name='InternalType_Testdd',
  full_name='xlsc.goods.GOODS_CONF.InternalType_Test.InternalType_Testdd',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='max_plural_num', full_name='xlsc.goods.GOODS_CONF.InternalType_Test.InternalType_Testdd.max_plural_num', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rarity', full_name='xlsc.goods.GOODS_CONF.InternalType_Test.InternalType_Testdd.rarity', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=521,
  serialized_end=585,
)

_GOODS_CONF_INTERNALTYPE_TEST = _descriptor.Descriptor(
  name='InternalType_Test',
  full_name='xlsc.goods.GOODS_CONF.InternalType_Test',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='is_plural', full_name='xlsc.goods.GOODS_CONF.InternalType_Test.is_plural', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Testdd', full_name='xlsc.goods.GOODS_CONF.InternalType_Test.Testdd', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='desc', full_name='xlsc.goods.GOODS_CONF.InternalType_Test.desc', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='color', full_name='xlsc.goods.GOODS_CONF.InternalType_Test.color', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='desc_list', full_name='xlsc.goods.GOODS_CONF.InternalType_Test.desc_list', index=4,
      number=5, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_GOODS_CONF_INTERNALTYPE_TEST_INTERNALTYPE_TESTDD, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=349,
  serialized_end=585,
)

_GOODS_CONF = _descriptor.Descriptor(
  name='GOODS_CONF',
  full_name='xlsc.goods.GOODS_CONF',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='xlsc.goods.GOODS_CONF.id', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='xlsc.goods.GOODS_CONF.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='short_name', full_name='xlsc.goods.GOODS_CONF.short_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Test', full_name='xlsc.goods.GOODS_CONF.Test', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='resource', full_name='xlsc.goods.GOODS_CONF.resource', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='xlsc.goods.GOODS_CONF.type', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='up_shelves_time', full_name='xlsc.goods.GOODS_CONF.up_shelves_time', index=6,
      number=7, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='off_shelves_time', full_name='xlsc.goods.GOODS_CONF.off_shelves_time', index=7,
      number=8, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sex_detail', full_name='xlsc.goods.GOODS_CONF.sex_detail', index=8,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='is_time_limit', full_name='xlsc.goods.GOODS_CONF.is_time_limit', index=9,
      number=10, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='smallIconType', full_name='xlsc.goods.GOODS_CONF.smallIconType', index=10,
      number=11, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='smallIconName', full_name='xlsc.goods.GOODS_CONF.smallIconName', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_GOODS_CONF_INTERNALTYPE_TEST, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=57,
  serialized_end=585,
)


_GOODS_CONF_ARRAY = _descriptor.Descriptor(
  name='GOODS_CONF_ARRAY',
  full_name='xlsc.goods.GOODS_CONF_ARRAY',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='items', full_name='xlsc.goods.GOODS_CONF_ARRAY.items', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=587,
  serialized_end=644,
)

_GOODS_CONF_INTERNALTYPE_TEST_INTERNALTYPE_TESTDD.containing_type = _GOODS_CONF_INTERNALTYPE_TEST
_GOODS_CONF_INTERNALTYPE_TEST.fields_by_name['Testdd'].message_type = _GOODS_CONF_INTERNALTYPE_TEST_INTERNALTYPE_TESTDD
_GOODS_CONF_INTERNALTYPE_TEST.containing_type = _GOODS_CONF
_GOODS_CONF.fields_by_name['Test'].message_type = _GOODS_CONF_INTERNALTYPE_TEST
_GOODS_CONF_ARRAY.fields_by_name['items'].message_type = _GOODS_CONF
DESCRIPTOR.message_types_by_name['GOODS_CONF'] = _GOODS_CONF
DESCRIPTOR.message_types_by_name['GOODS_CONF_ARRAY'] = _GOODS_CONF_ARRAY

GOODS_CONF = _reflection.GeneratedProtocolMessageType('GOODS_CONF', (_message.Message,), dict(

  InternalType_Test = _reflection.GeneratedProtocolMessageType('InternalType_Test', (_message.Message,), dict(

    InternalType_Testdd = _reflection.GeneratedProtocolMessageType('InternalType_Testdd', (_message.Message,), dict(
      DESCRIPTOR = _GOODS_CONF_INTERNALTYPE_TEST_INTERNALTYPE_TESTDD,
      __module__ = 'output.proto.xlsc_goods_goods_conf_pb2'
      # @@protoc_insertion_point(class_scope:xlsc.goods.GOODS_CONF.InternalType_Test.InternalType_Testdd)
      ))
    ,
    DESCRIPTOR = _GOODS_CONF_INTERNALTYPE_TEST,
    __module__ = 'output.proto.xlsc_goods_goods_conf_pb2'
    # @@protoc_insertion_point(class_scope:xlsc.goods.GOODS_CONF.InternalType_Test)
    ))
  ,
  DESCRIPTOR = _GOODS_CONF,
  __module__ = 'output.proto.xlsc_goods_goods_conf_pb2'
  # @@protoc_insertion_point(class_scope:xlsc.goods.GOODS_CONF)
  ))
_sym_db.RegisterMessage(GOODS_CONF)
_sym_db.RegisterMessage(GOODS_CONF.InternalType_Test)
_sym_db.RegisterMessage(GOODS_CONF.InternalType_Test.InternalType_Testdd)

GOODS_CONF_ARRAY = _reflection.GeneratedProtocolMessageType('GOODS_CONF_ARRAY', (_message.Message,), dict(
  DESCRIPTOR = _GOODS_CONF_ARRAY,
  __module__ = 'output.proto.xlsc_goods_goods_conf_pb2'
  # @@protoc_insertion_point(class_scope:xlsc.goods.GOODS_CONF_ARRAY)
  ))
_sym_db.RegisterMessage(GOODS_CONF_ARRAY)


# @@protoc_insertion_point(module_scope)

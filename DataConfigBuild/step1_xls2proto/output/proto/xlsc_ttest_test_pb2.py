# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: output/proto/xlsc_ttest_test.proto

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
  name='output/proto/xlsc_ttest_test.proto',
  package='xlsc.ttest',
  serialized_pb=_b('\n\"output/proto/xlsc_ttest_test.proto\x12\nxlsc.ttest\".\n\x04TEST\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0c\n\x04icon\x18\x03 \x01(\x05\"-\n\nTEST_ARRAY\x12\x1f\n\x05items\x18\x01 \x03(\x0b\x32\x10.xlsc.ttest.TEST')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_TEST = _descriptor.Descriptor(
  name='TEST',
  full_name='xlsc.ttest.TEST',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='xlsc.ttest.TEST.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='xlsc.ttest.TEST.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='icon', full_name='xlsc.ttest.TEST.icon', index=2,
      number=3, type=5, cpp_type=1, label=1,
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
  serialized_start=50,
  serialized_end=96,
)


_TEST_ARRAY = _descriptor.Descriptor(
  name='TEST_ARRAY',
  full_name='xlsc.ttest.TEST_ARRAY',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='items', full_name='xlsc.ttest.TEST_ARRAY.items', index=0,
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
  serialized_start=98,
  serialized_end=143,
)

_TEST_ARRAY.fields_by_name['items'].message_type = _TEST
DESCRIPTOR.message_types_by_name['TEST'] = _TEST
DESCRIPTOR.message_types_by_name['TEST_ARRAY'] = _TEST_ARRAY

TEST = _reflection.GeneratedProtocolMessageType('TEST', (_message.Message,), dict(
  DESCRIPTOR = _TEST,
  __module__ = 'output.proto.xlsc_ttest_test_pb2'
  # @@protoc_insertion_point(class_scope:xlsc.ttest.TEST)
  ))
_sym_db.RegisterMessage(TEST)

TEST_ARRAY = _reflection.GeneratedProtocolMessageType('TEST_ARRAY', (_message.Message,), dict(
  DESCRIPTOR = _TEST_ARRAY,
  __module__ = 'output.proto.xlsc_ttest_test_pb2'
  # @@protoc_insertion_point(class_scope:xlsc.ttest.TEST_ARRAY)
  ))
_sym_db.RegisterMessage(TEST_ARRAY)


# @@protoc_insertion_point(module_scope)
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: message.proto

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
  name='message.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\rmessage.proto\"+\n\x0bPhoneNumber\x12\x0e\n\x06number\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x02 \x01(\t\"5\n\tBirthDate\x12\x0c\n\x04year\x18\x01 \x01(\x05\x12\r\n\x05month\x18\x02 \x01(\x05\x12\x0b\n\x03\x64\x61y\x18\x03 \x01(\x05\"\xa6\x01\n\x06Person\x12\n\n\x02id\x18\x01 \x01(\t\x12\x10\n\x08isActive\x18\x02 \x01(\x08\x12\x0b\n\x03\x61ge\x18\x03 \x01(\x05\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x0f\n\x07\x61\x64\x64ress\x18\x05 \x01(\t\x12\r\n\x05\x61\x62out\x18\x06 \x01(\t\x12#\n\rphone_numbers\x18\x07 \x03(\x0b\x32\x0c.PhoneNumber\x12\x1e\n\nbirth_date\x18\x08 \x01(\x0b\x32\n.BirthDateb\x06proto3')
)




_PHONENUMBER = _descriptor.Descriptor(
  name='PhoneNumber',
  full_name='PhoneNumber',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='number', full_name='PhoneNumber.number', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='PhoneNumber.type', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=17,
  serialized_end=60,
)


_BIRTHDATE = _descriptor.Descriptor(
  name='BirthDate',
  full_name='BirthDate',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='year', full_name='BirthDate.year', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='month', full_name='BirthDate.month', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='day', full_name='BirthDate.day', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=62,
  serialized_end=115,
)


_PERSON = _descriptor.Descriptor(
  name='Person',
  full_name='Person',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='Person.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='isActive', full_name='Person.isActive', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='age', full_name='Person.age', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='Person.name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='address', full_name='Person.address', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='about', full_name='Person.about', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='phone_numbers', full_name='Person.phone_numbers', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='birth_date', full_name='Person.birth_date', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=118,
  serialized_end=284,
)

_PERSON.fields_by_name['phone_numbers'].message_type = _PHONENUMBER
_PERSON.fields_by_name['birth_date'].message_type = _BIRTHDATE
DESCRIPTOR.message_types_by_name['PhoneNumber'] = _PHONENUMBER
DESCRIPTOR.message_types_by_name['BirthDate'] = _BIRTHDATE
DESCRIPTOR.message_types_by_name['Person'] = _PERSON
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PhoneNumber = _reflection.GeneratedProtocolMessageType('PhoneNumber', (_message.Message,), dict(
  DESCRIPTOR = _PHONENUMBER,
  __module__ = 'message_pb2'
  # @@protoc_insertion_point(class_scope:PhoneNumber)
  ))
_sym_db.RegisterMessage(PhoneNumber)

BirthDate = _reflection.GeneratedProtocolMessageType('BirthDate', (_message.Message,), dict(
  DESCRIPTOR = _BIRTHDATE,
  __module__ = 'message_pb2'
  # @@protoc_insertion_point(class_scope:BirthDate)
  ))
_sym_db.RegisterMessage(BirthDate)

Person = _reflection.GeneratedProtocolMessageType('Person', (_message.Message,), dict(
  DESCRIPTOR = _PERSON,
  __module__ = 'message_pb2'
  # @@protoc_insertion_point(class_scope:Person)
  ))
_sym_db.RegisterMessage(Person)


# @@protoc_insertion_point(module_scope)

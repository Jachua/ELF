# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: play.proto

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
  name='play.proto',
  package='play',
  syntax='proto3',
  serialized_pb=_b('\n\nplay.proto\x12\x04play\":\n\x04Step\x12\t\n\x01x\x18\x01 \x01(\r\x12\t\n\x01y\x18\x02 \x01(\r\x12\x1c\n\x06player\x18\x03 \x01(\x0b\x32\x0c.play.Player\"\x17\n\x06Player\x12\r\n\x05\x63olor\x18\x01 \x01(\r\"\x17\n\x05State\x12\x0e\n\x06status\x18\x01 \x01(\x08\"\x17\n\x07Resumed\x12\x0c\n\x04move\x18\x01 \x03(\t2\xaa\x03\n\x04Turn\x12$\n\x07SetMove\x12\n.play.Step\x1a\x0b.play.State\"\x00\x12%\n\x07GetMove\x12\x0c.play.Player\x1a\n.play.Step\"\x00\x12(\n\nUpdateNext\x12\x0b.play.State\x1a\x0b.play.State\"\x00\x12+\n\x0cIsNextPlayer\x12\x0c.play.Player\x1a\x0b.play.State\"\x00\x12(\n\tSetPlayer\x12\x0c.play.Player\x1a\x0b.play.State\"\x00\x12*\n\x0bGetAIPlayer\x12\x0b.play.State\x1a\x0c.play.Player\"\x00\x12\'\n\tHasChosen\x12\x0b.play.State\x1a\x0b.play.State\"\x00\x12\'\n\x08HasMoved\x12\x0c.play.Player\x1a\x0b.play.State\"\x00\x12*\n\nSetResumed\x12\r.play.Resumed\x1a\x0b.play.State\"\x00\x12*\n\nGetResumed\x12\x0b.play.State\x1a\r.play.Resumed\"\x00\x62\x06proto3')
)




_STEP = _descriptor.Descriptor(
  name='Step',
  full_name='play.Step',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='play.Step.x', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='y', full_name='play.Step.y', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='player', full_name='play.Step.player', index=2,
      number=3, type=11, cpp_type=10, label=1,
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
  serialized_start=20,
  serialized_end=78,
)


_PLAYER = _descriptor.Descriptor(
  name='Player',
  full_name='play.Player',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='color', full_name='play.Player.color', index=0,
      number=1, type=13, cpp_type=3, label=1,
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
  serialized_start=80,
  serialized_end=103,
)


_STATE = _descriptor.Descriptor(
  name='State',
  full_name='play.State',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='play.State.status', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=105,
  serialized_end=128,
)


_RESUMED = _descriptor.Descriptor(
  name='Resumed',
  full_name='play.Resumed',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='move', full_name='play.Resumed.move', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=130,
  serialized_end=153,
)

_STEP.fields_by_name['player'].message_type = _PLAYER
DESCRIPTOR.message_types_by_name['Step'] = _STEP
DESCRIPTOR.message_types_by_name['Player'] = _PLAYER
DESCRIPTOR.message_types_by_name['State'] = _STATE
DESCRIPTOR.message_types_by_name['Resumed'] = _RESUMED
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Step = _reflection.GeneratedProtocolMessageType('Step', (_message.Message,), dict(
  DESCRIPTOR = _STEP,
  __module__ = 'play_pb2'
  # @@protoc_insertion_point(class_scope:play.Step)
  ))
_sym_db.RegisterMessage(Step)

Player = _reflection.GeneratedProtocolMessageType('Player', (_message.Message,), dict(
  DESCRIPTOR = _PLAYER,
  __module__ = 'play_pb2'
  # @@protoc_insertion_point(class_scope:play.Player)
  ))
_sym_db.RegisterMessage(Player)

State = _reflection.GeneratedProtocolMessageType('State', (_message.Message,), dict(
  DESCRIPTOR = _STATE,
  __module__ = 'play_pb2'
  # @@protoc_insertion_point(class_scope:play.State)
  ))
_sym_db.RegisterMessage(State)

Resumed = _reflection.GeneratedProtocolMessageType('Resumed', (_message.Message,), dict(
  DESCRIPTOR = _RESUMED,
  __module__ = 'play_pb2'
  # @@protoc_insertion_point(class_scope:play.Resumed)
  ))
_sym_db.RegisterMessage(Resumed)



_TURN = _descriptor.ServiceDescriptor(
  name='Turn',
  full_name='play.Turn',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=156,
  serialized_end=582,
  methods=[
  _descriptor.MethodDescriptor(
    name='SetMove',
    full_name='play.Turn.SetMove',
    index=0,
    containing_service=None,
    input_type=_STEP,
    output_type=_STATE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetMove',
    full_name='play.Turn.GetMove',
    index=1,
    containing_service=None,
    input_type=_PLAYER,
    output_type=_STEP,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='UpdateNext',
    full_name='play.Turn.UpdateNext',
    index=2,
    containing_service=None,
    input_type=_STATE,
    output_type=_STATE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='IsNextPlayer',
    full_name='play.Turn.IsNextPlayer',
    index=3,
    containing_service=None,
    input_type=_PLAYER,
    output_type=_STATE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='SetPlayer',
    full_name='play.Turn.SetPlayer',
    index=4,
    containing_service=None,
    input_type=_PLAYER,
    output_type=_STATE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetAIPlayer',
    full_name='play.Turn.GetAIPlayer',
    index=5,
    containing_service=None,
    input_type=_STATE,
    output_type=_PLAYER,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='HasChosen',
    full_name='play.Turn.HasChosen',
    index=6,
    containing_service=None,
    input_type=_STATE,
    output_type=_STATE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='HasMoved',
    full_name='play.Turn.HasMoved',
    index=7,
    containing_service=None,
    input_type=_PLAYER,
    output_type=_STATE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='SetResumed',
    full_name='play.Turn.SetResumed',
    index=8,
    containing_service=None,
    input_type=_RESUMED,
    output_type=_STATE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetResumed',
    full_name='play.Turn.GetResumed',
    index=9,
    containing_service=None,
    input_type=_STATE,
    output_type=_RESUMED,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_TURN)

DESCRIPTOR.services_by_name['Turn'] = _TURN

# @@protoc_insertion_point(module_scope)

# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: histogram.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='histogram.proto',
  package='physt',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0fhistogram.proto\x12\x05physt\"\x9f\x01\n\x04Meta\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12\x12\n\naxis_names\x18\x03 \x03(\t\x12\x32\n\x0cuser_defined\x18\x04 \x03(\x0b\x32\x1c.physt.Meta.UserDefinedEntry\x1a\x32\n\x10UserDefinedEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\")\n\tBinLimits\x12\r\n\x05lower\x18\x01 \x01(\x01\x12\r\n\x05upper\x18\x02 \x01(\x01\"Q\n\x07\x42inning\x12\x10\n\x08\x61\x64\x61ptive\x18\x01 \x01(\x08\x12\x14\n\x0c\x62inning_type\x18\x02 \x01(\t\x12\x1e\n\x04\x62ins\x18\x03 \x03(\x0b\x32\x10.physt.BinLimits\"\xeb\x01\n\tHistogram\x12\x16\n\x0ehistogram_type\x18\x01 \x01(\t\x12 \n\x08\x62innings\x18\x02 \x03(\x0b\x32\x0e.physt.Binning\x12\x13\n\x0b\x66requencies\x18\x03 \x03(\x01\x12\r\n\x05\x64type\x18\x04 \x01(\t\x12\x0f\n\x07\x65rrors2\x18\x05 \x03(\x01\x12\x19\n\x04meta\x18\x06 \x01(\x0b\x32\x0b.physt.Meta\x12\x0e\n\x06missed\x18\x07 \x03(\x01\x12\x13\n\x0bmissed_keep\x18\x08 \x01(\x08\x12\x15\n\rphyst_version\x18\t \x01(\t\x12\x18\n\x10physt_compatible\x18\n \x01(\t\"\x9a\x01\n\x13HistogramCollection\x12>\n\nhistograms\x18\x01 \x03(\x0b\x32*.physt.HistogramCollection.HistogramsEntry\x1a\x43\n\x0fHistogramsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x1f\n\x05value\x18\x02 \x01(\x0b\x32\x10.physt.Histogram:\x02\x38\x01\x62\x06proto3')
)




_META_USERDEFINEDENTRY = _descriptor.Descriptor(
  name='UserDefinedEntry',
  full_name='physt.Meta.UserDefinedEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='physt.Meta.UserDefinedEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='physt.Meta.UserDefinedEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=136,
  serialized_end=186,
)

_META = _descriptor.Descriptor(
  name='Meta',
  full_name='physt.Meta',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='physt.Meta.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='title', full_name='physt.Meta.title', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='axis_names', full_name='physt.Meta.axis_names', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_defined', full_name='physt.Meta.user_defined', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_META_USERDEFINEDENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=27,
  serialized_end=186,
)


_BINLIMITS = _descriptor.Descriptor(
  name='BinLimits',
  full_name='physt.BinLimits',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='lower', full_name='physt.BinLimits.lower', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='upper', full_name='physt.BinLimits.upper', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=188,
  serialized_end=229,
)


_BINNING = _descriptor.Descriptor(
  name='Binning',
  full_name='physt.Binning',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='adaptive', full_name='physt.Binning.adaptive', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='binning_type', full_name='physt.Binning.binning_type', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bins', full_name='physt.Binning.bins', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=231,
  serialized_end=312,
)


_HISTOGRAM = _descriptor.Descriptor(
  name='Histogram',
  full_name='physt.Histogram',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='histogram_type', full_name='physt.Histogram.histogram_type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='binnings', full_name='physt.Histogram.binnings', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='frequencies', full_name='physt.Histogram.frequencies', index=2,
      number=3, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dtype', full_name='physt.Histogram.dtype', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='errors2', full_name='physt.Histogram.errors2', index=4,
      number=5, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='meta', full_name='physt.Histogram.meta', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='missed', full_name='physt.Histogram.missed', index=6,
      number=7, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='missed_keep', full_name='physt.Histogram.missed_keep', index=7,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='physt_version', full_name='physt.Histogram.physt_version', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='physt_compatible', full_name='physt.Histogram.physt_compatible', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=315,
  serialized_end=550,
)


_HISTOGRAMCOLLECTION_HISTOGRAMSENTRY = _descriptor.Descriptor(
  name='HistogramsEntry',
  full_name='physt.HistogramCollection.HistogramsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='physt.HistogramCollection.HistogramsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='physt.HistogramCollection.HistogramsEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=640,
  serialized_end=707,
)

_HISTOGRAMCOLLECTION = _descriptor.Descriptor(
  name='HistogramCollection',
  full_name='physt.HistogramCollection',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='histograms', full_name='physt.HistogramCollection.histograms', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_HISTOGRAMCOLLECTION_HISTOGRAMSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=553,
  serialized_end=707,
)

_META_USERDEFINEDENTRY.containing_type = _META
_META.fields_by_name['user_defined'].message_type = _META_USERDEFINEDENTRY
_BINNING.fields_by_name['bins'].message_type = _BINLIMITS
_HISTOGRAM.fields_by_name['binnings'].message_type = _BINNING
_HISTOGRAM.fields_by_name['meta'].message_type = _META
_HISTOGRAMCOLLECTION_HISTOGRAMSENTRY.fields_by_name['value'].message_type = _HISTOGRAM
_HISTOGRAMCOLLECTION_HISTOGRAMSENTRY.containing_type = _HISTOGRAMCOLLECTION
_HISTOGRAMCOLLECTION.fields_by_name['histograms'].message_type = _HISTOGRAMCOLLECTION_HISTOGRAMSENTRY
DESCRIPTOR.message_types_by_name['Meta'] = _META
DESCRIPTOR.message_types_by_name['BinLimits'] = _BINLIMITS
DESCRIPTOR.message_types_by_name['Binning'] = _BINNING
DESCRIPTOR.message_types_by_name['Histogram'] = _HISTOGRAM
DESCRIPTOR.message_types_by_name['HistogramCollection'] = _HISTOGRAMCOLLECTION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Meta = _reflection.GeneratedProtocolMessageType('Meta', (_message.Message,), dict(

  UserDefinedEntry = _reflection.GeneratedProtocolMessageType('UserDefinedEntry', (_message.Message,), dict(
    DESCRIPTOR = _META_USERDEFINEDENTRY,
    __module__ = 'histogram_pb2'
    # @@protoc_insertion_point(class_scope:physt.Meta.UserDefinedEntry)
    ))
  ,
  DESCRIPTOR = _META,
  __module__ = 'histogram_pb2'
  # @@protoc_insertion_point(class_scope:physt.Meta)
  ))
_sym_db.RegisterMessage(Meta)
_sym_db.RegisterMessage(Meta.UserDefinedEntry)

BinLimits = _reflection.GeneratedProtocolMessageType('BinLimits', (_message.Message,), dict(
  DESCRIPTOR = _BINLIMITS,
  __module__ = 'histogram_pb2'
  # @@protoc_insertion_point(class_scope:physt.BinLimits)
  ))
_sym_db.RegisterMessage(BinLimits)

Binning = _reflection.GeneratedProtocolMessageType('Binning', (_message.Message,), dict(
  DESCRIPTOR = _BINNING,
  __module__ = 'histogram_pb2'
  # @@protoc_insertion_point(class_scope:physt.Binning)
  ))
_sym_db.RegisterMessage(Binning)

Histogram = _reflection.GeneratedProtocolMessageType('Histogram', (_message.Message,), dict(
  DESCRIPTOR = _HISTOGRAM,
  __module__ = 'histogram_pb2'
  # @@protoc_insertion_point(class_scope:physt.Histogram)
  ))
_sym_db.RegisterMessage(Histogram)

HistogramCollection = _reflection.GeneratedProtocolMessageType('HistogramCollection', (_message.Message,), dict(

  HistogramsEntry = _reflection.GeneratedProtocolMessageType('HistogramsEntry', (_message.Message,), dict(
    DESCRIPTOR = _HISTOGRAMCOLLECTION_HISTOGRAMSENTRY,
    __module__ = 'histogram_pb2'
    # @@protoc_insertion_point(class_scope:physt.HistogramCollection.HistogramsEntry)
    ))
  ,
  DESCRIPTOR = _HISTOGRAMCOLLECTION,
  __module__ = 'histogram_pb2'
  # @@protoc_insertion_point(class_scope:physt.HistogramCollection)
  ))
_sym_db.RegisterMessage(HistogramCollection)
_sym_db.RegisterMessage(HistogramCollection.HistogramsEntry)


_META_USERDEFINEDENTRY._options = None
_HISTOGRAMCOLLECTION_HISTOGRAMSENTRY._options = None
# @@protoc_insertion_point(module_scope)
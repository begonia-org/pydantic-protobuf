# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: options.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\roptions.proto\x12\x08pydantic\x1a google/protobuf/descriptor.proto\"\xa2\x03\n\nAnnotation\x12\x13\n\x0b\x64\x65scription\x18\x01 \x01(\t\x12\x0f\n\x07\x65xample\x18\x02 \x01(\t\x12\x0f\n\x07\x64\x65\x66\x61ult\x18\x03 \x01(\t\x12\r\n\x05\x61lias\x18\x04 \x01(\t\x12\r\n\x05title\x18\x05 \x01(\t\x12\x10\n\x08required\x18\x06 \x01(\x08\x12\x10\n\x08nullable\x18\x07 \x01(\x08\x12 \n\x0bprimary_key\x18\x08 \x01(\x08R\x0bprimary_key\x12\x0e\n\x06unique\x18\t \x01(\x08\x12\r\n\x05index\x18\n \x01(\x08\x12\r\n\x05\x63onst\x18\x12 \x01(\x08\x12\x1e\n\nfield_type\x18\x0b \x01(\tR\nfield_type\x12&\n\x0esa_column_type\x18\x14 \x01(\tR\x0esa_column_type\x12\x1e\n\nmin_length\x18\x0c \x01(\x05R\nmin_length\x12\x1e\n\nmax_length\x18\r \x01(\x05R\nmax_length\x12\n\n\x02gt\x18\x0e \x01(\x01\x12\n\n\x02ge\x18\x0f \x01(\x01\x12\n\n\x02lt\x18\x10 \x01(\x01\x12\n\n\x02le\x18\x11 \x01(\x01\x12\x13\n\x0b\x66oreign_key\x18\x13 \x01(\t\"[\n\rCompoundIndex\x12\x16\n\x06indexs\x18\x01 \x03(\tR\x06indexs\x12\x1e\n\nindex_type\x18\x02 \x01(\tR\nindex_type\x12\x12\n\x04name\x18\x03 \x01(\tR\x04name\"u\n\x12\x44\x61tabaseAnnotation\x12\x1e\n\ntable_name\x18\x01 \x01(\tR\ntable_name\x12?\n\x0e\x63ompound_index\x18\x02 \x03(\x0b\x32\x17.pydantic.CompoundIndexR\x0e\x63ompound_index:Q\n\x08\x64\x61tabase\x12\x1f.google.protobuf.MessageOptions\x18\x99\x88\x03 \x01(\x0b\x32\x1c.pydantic.DatabaseAnnotation:D\n\x05\x66ield\x12\x1d.google.protobuf.FieldOptions\x18\xb5\x87\x03 \x01(\x0b\x32\x14.pydantic.Annotationb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'options_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
  google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(database)
  google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(field)

  DESCRIPTOR._options = None
  _ANNOTATION._serialized_start=62
  _ANNOTATION._serialized_end=480
  _COMPOUNDINDEX._serialized_start=482
  _COMPOUNDINDEX._serialized_end=573
  _DATABASEANNOTATION._serialized_start=575
  _DATABASEANNOTATION._serialized_end=692
# @@protoc_insertion_point(module_scope)

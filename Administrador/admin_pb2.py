# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: admin.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0b\x61\x64min.proto\"?\n\x15inserirClienteRequest\x12\x10\n\x08\x63lientId\x18\x01 \x01(\t\x12\x14\n\x0c\x64\x61\x64osCliente\x18\x02 \x01(\t\"&\n\x13inserirClienteReply\x12\x0f\n\x07message\x18\x01 \x01(\t\"A\n\x17modificarClienteRequest\x12\x10\n\x08\x63lientId\x18\x01 \x01(\t\x12\x14\n\x0c\x64\x61\x64osCliente\x18\x02 \x01(\t\"(\n\x15modificarClienteReply\x12\x0f\n\x07message\x18\x01 \x01(\t\"+\n\x17recuperarClienteRequest\x12\x10\n\x08\x63lientId\x18\x01 \x01(\t\"(\n\x15recuperarClienteReply\x12\x0f\n\x07message\x18\x01 \x01(\t\"(\n\x14\x61pagarClienteRequest\x12\x10\n\x08\x63lientId\x18\x01 \x01(\t\"%\n\x12\x61pagarClienteReply\x12\x0f\n\x07message\x18\x01 \x01(\t\"@\n\x15inserirProdutoRequest\x12\x11\n\tprodutoId\x18\x01 \x01(\t\x12\x14\n\x0c\x64\x61\x64osProduto\x18\x02 \x01(\t\"&\n\x13inserirProdutoReply\x12\x0f\n\x07message\x18\x01 \x01(\t\"B\n\x17modificarProdutoRequest\x12\x11\n\tprodutoId\x18\x01 \x01(\t\x12\x14\n\x0c\x64\x61\x64osProduto\x18\x02 \x01(\t\"(\n\x15modificarProdutoReply\x12\x0f\n\x07message\x18\x01 \x01(\t\",\n\x17recuperarProdutoRequest\x12\x11\n\tprodutoId\x18\x01 \x01(\t\"(\n\x15recuperarProdutoReply\x12\x0f\n\x07message\x18\x01 \x01(\t\")\n\x14\x61pagarProdutoRequest\x12\x11\n\tprodutoId\x18\x01 \x01(\t\"%\n\x12\x61pagarProdutoReply\x12\x0f\n\x07message\x18\x01 \x01(\t2\x99\x04\n\x05\x41\x64min\x12>\n\x0einserirCliente\x12\x16.inserirClienteRequest\x1a\x14.inserirClienteReply\x12\x44\n\x10modificarCliente\x12\x18.modificarClienteRequest\x1a\x16.modificarClienteReply\x12\x44\n\x10recuperarCliente\x12\x18.recuperarClienteRequest\x1a\x16.recuperarClienteReply\x12;\n\rapagarCliente\x12\x15.apagarClienteRequest\x1a\x13.apagarClienteReply\x12>\n\x0einserirProduto\x12\x16.inserirProdutoRequest\x1a\x14.inserirProdutoReply\x12\x44\n\x10modificarProduto\x12\x18.modificarProdutoRequest\x1a\x16.modificarProdutoReply\x12\x44\n\x10recuperarProduto\x12\x18.recuperarProdutoRequest\x1a\x16.recuperarProdutoReply\x12;\n\rapagarProduto\x12\x15.apagarProdutoRequest\x1a\x13.apagarProdutoReplyb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'admin_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _INSERIRCLIENTEREQUEST._serialized_start=15
  _INSERIRCLIENTEREQUEST._serialized_end=78
  _INSERIRCLIENTEREPLY._serialized_start=80
  _INSERIRCLIENTEREPLY._serialized_end=118
  _MODIFICARCLIENTEREQUEST._serialized_start=120
  _MODIFICARCLIENTEREQUEST._serialized_end=185
  _MODIFICARCLIENTEREPLY._serialized_start=187
  _MODIFICARCLIENTEREPLY._serialized_end=227
  _RECUPERARCLIENTEREQUEST._serialized_start=229
  _RECUPERARCLIENTEREQUEST._serialized_end=272
  _RECUPERARCLIENTEREPLY._serialized_start=274
  _RECUPERARCLIENTEREPLY._serialized_end=314
  _APAGARCLIENTEREQUEST._serialized_start=316
  _APAGARCLIENTEREQUEST._serialized_end=356
  _APAGARCLIENTEREPLY._serialized_start=358
  _APAGARCLIENTEREPLY._serialized_end=395
  _INSERIRPRODUTOREQUEST._serialized_start=397
  _INSERIRPRODUTOREQUEST._serialized_end=461
  _INSERIRPRODUTOREPLY._serialized_start=463
  _INSERIRPRODUTOREPLY._serialized_end=501
  _MODIFICARPRODUTOREQUEST._serialized_start=503
  _MODIFICARPRODUTOREQUEST._serialized_end=569
  _MODIFICARPRODUTOREPLY._serialized_start=571
  _MODIFICARPRODUTOREPLY._serialized_end=611
  _RECUPERARPRODUTOREQUEST._serialized_start=613
  _RECUPERARPRODUTOREQUEST._serialized_end=657
  _RECUPERARPRODUTOREPLY._serialized_start=659
  _RECUPERARPRODUTOREPLY._serialized_end=699
  _APAGARPRODUTOREQUEST._serialized_start=701
  _APAGARPRODUTOREQUEST._serialized_end=742
  _APAGARPRODUTOREPLY._serialized_start=744
  _APAGARPRODUTOREPLY._serialized_end=781
  _ADMIN._serialized_start=784
  _ADMIN._serialized_end=1321
# @@protoc_insertion_point(module_scope)

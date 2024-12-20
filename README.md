# grpc using different approaches to a monorepo

## 2024/12/01 - simpler solutions first

- start with `uv` workspaces
- trying to compile proto files when building a python distribution turned out to be a bit tricky
- `grpcio-tools` provides a setuptools command that can be used to automatically create stubs from the source tree
- this requires dealing with python package data to some extend
- python considers files tracked by git as part of package data as long as they are part of the source tree
- otherwise they need to be included explicitly using `package_data` directive of `setup`


## 2024/11/30 - trying out bazel

- difficulty figuring out which rules to use, this link https://registry.bazel.build/modules/protobuf helped a bit
- turns out `py_proto_library` is part of `rules_python` (at least since verison `0.40.0`)
- using https://www.velotio.com/engineering-blog/grpc-implementation-using-python as an example gRPC thing
- figuring out which version of `clang` to use can be a pain (at least on MacOS) which is felt when trying to compile
rulesets
- `clang-17` did not work, now tried with `brew install llvm@15` and `CC=/opt/homebrew/opt/llvm@15/bin/clang` before
running `bazel build //...` -> this WORKED!
- configurin lsps to work with bazel involves querying for associated files for python imports ([example pyright
config](https://github.com/alexander-born/.cfg/blob/07644649215a15e7cecdef0265142b3ac4f23905/nvim/.config/nvim/lua/config/bazel.lua#L87))
- bazel build doesn't output generated files to the source tree so they are not checked into source code
- trying to find a way to generate the grpc related code, found: https://github.com/grpc/grpc, also this blog https://grpc.io/blog/bazel-rules-protobuf/#23-protobuf-definitions that
has more info
- maybe I don't understand the relationship between grpc and protobuf yet
- after working on this for a bit, maybe bazel is not something to start a project with -> start with a simpler layout,
  maybe test using uv for a monorepo
#### having a look at the generated code:
```python
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: src/message.proto
# Protobuf Python Version: 5.29.0-rc2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    0,
    '-rc2',
    'src/message.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11src/message.proto\x12\x05unary\"\x1a\n\x07Message\x12\x0f\n\x07message\x18\x01 \x01(\t\"4\n\x0fMessageResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x10\n\x08received\x18\x02 \x01(\x08\x32\x46\n\x05Unary\x12=\n\x11GetServerResponse\x12\x0e.unary.Message\x1a\x16.unary.MessageResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'src.message_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_MESSAGE']._serialized_start=28
  _globals['_MESSAGE']._serialized_end=54
  _globals['_MESSAGERESPONSE']._serialized_start=56
  _globals['_MESSAGERESPONSE']._serialized_end=108
  _globals['_UNARY']._serialized_start=110
  _globals['_UNARY']._serialized_end=180
# @@protoc_insertion_point(module_scope)
```
the imports `google.protobuf` are made available by installing the `protobuf` package from pypi

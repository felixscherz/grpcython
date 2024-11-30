# grpc built with bazel

## 2024/11/30

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

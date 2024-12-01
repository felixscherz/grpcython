import grpc_tools.command
import setuptools
from setuptools import Command
from setuptools.command import build


class BuildHook(build.build):
    def run(self):
        self.run_command("build_proto_modules")
        build.build.run(self)


setuptools.setup(
    # these only need to be set if the files are not part of version control i.e. not tracked by git
    # include_package_data=True,
    # package_data={"": ["*.proto"]},
    cmdclass={
        "build_proto_modules": grpc_tools.command.BuildPackageProtos,
        "build": BuildHook,
    },
)

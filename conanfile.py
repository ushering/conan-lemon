#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, CMake, tools
import os
import shutil

class LemonConan(ConanFile):
    name = "lemon"
    version = "1.3.1_src"
    url = "https://github.com/ushering/conan-lemon"
    license = "Boost Software License"
    author = "Ruisheng Wang <ruisheng.wang@outlook.com>"
    homepage = "https://lemon.cs.elte.hu/trac/lemon"
    description = "LEMON stands for Library for Efficient Modeling and Optimization in Networks. It is a C++ template library providing efficient implementations of common data structures and algorithms with focus on combinatorial optimization tasks connected mainly with graphs and networks."
    settings = "os", "compiler", "build_type", "arch"
    exports = "file.patch"
    _source_subfolder = "source_subfolder"
    exports_sources = os.path.join(_source_subfolder, '*')


    def _source(self):
        source_url = "http://lemon.cs.elte.hu/pub/sources/lemon-{}.tar.gz".format(self.version)
        tools.get(source_url, sha256="71b7c725f4c0b4a8ccb92eb87b208701586cf7a96156ebd821ca3ed855bad3c8")
        extracted_dir = self.name + "-" + self.version
        os.rename(extracted_dir, self._source_subfolder)
        tools.patch(base_path=self._source_subfolder, patch_file="file.patch")

    def _configure_cmake(self):
        cmake = CMake(self)
        cmake.definitions["BUILD_SHARED_LIBS"]="FALSE"
        cmake.configure(source_folder=self._source_subfolder)
        return cmake

    def build(self):
        cmake = self._configure_cmake()
        cmake.build()

    def package(self):
        cmake = self._configure_cmake()
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)

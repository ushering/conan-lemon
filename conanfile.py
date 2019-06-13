#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, CMake, tools
import os

class LemonConan(ConanFile):
    name = "lemon"
    version = "1.3.1"
    url = "https://github.com/ushering/conan-lemon"
    license = "Boost Software License"
    author = "Ruisheng Wang <ruisheng.wang@outlook.com>"
    homepage = "https://lemon.cs.elte.hu/trac/lemon"
    description = "LEMON stands for Library for Efficient Modeling and Optimization in Networks. It is a C++ template library providing efficient implementations of common data structures and algorithms with focus on combinatorial optimization tasks connected mainly with graphs and networks."
    settings = "os", "compiler", "build_type", "arch"
    source_subfolder = "source_subfolder"

    def source(self):
        source_url = "http://lemon.cs.elte.hu/pub/sources/lemon-{}.tar.gz".format(self.version)
        tools.get(source_url)
        extracted_dir = self.name + "-" + self.version
        os.rename(extracted_dir, self.source_subfolder)

    def _configure_cmake(self):
        cmake = CMake(self)
        cmake.configure(source_folder=self.source_subfolder)
        return cmake

    def build(self):
        cmake = self._configure_cmake()
        cmake.build()

    def package(self):
        cmake = self._configure_cmake()
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)

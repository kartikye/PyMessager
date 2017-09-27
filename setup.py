#!/usr/bin/python3
# -*- encoding: utf-8 -*-

from setuptools import setup

__author__ = "Kartikye Mittal"

setup(
    name="PyMessager",
    version="1.0.1",
    packages=["pymessager", ],
    license='The MIT License (MIT) Copyright © 2017 Engine Bai.',
    description="A Python SDK and Flask API to develop chatbot on Facebook Message Platform",
    long_description=open("README.md", "r").read(),
    author="Kartikye Mittal",
    author_email="kartikye.mittal@gmail.com",
    url="https://github.com/kartikye/PyMessager",
    install_requires=[
        "requests"
    ],
)

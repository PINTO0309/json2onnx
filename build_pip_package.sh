#!/bin/bash

rm -rf build/
rm -rf dist/
rm -rf json2onnx.egg-info/
python3 setup.py sdist bdist_wheel
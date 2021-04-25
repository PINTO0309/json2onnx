# json2onnx
Converts a JSON file to an ONNX file.

[![PyPI - Downloads](https://img.shields.io/pypi/dm/json2onnx?color=2BAF2B&label=Downloads%EF%BC%8FInstalled)](https://pypistats.org/packages/json2onnx) ![GitHub](https://img.shields.io/github/license/PINTO0309/json2onnx?color=2BAF2B) [![PyPI](https://img.shields.io/pypi/v/json2onnx?color=2BAF2B)](https://pypi.org/project/json2onnx/)

## 1. Install

```
$ pip install protobuf onnx
$ pip install json2onnx --upgrade
```

## 2. Usage

```
json2onnx [-h] \
  --json_path JSON_PATH \
  [--model_path MODEL_PATH]

optional arguments:
  -h, --help
                        show this help message and exit
  --json_path JSON_PATH
                        Input JSON file path (*.json)
  --model_path MODEL_PATH
                        Output ONNX model path (*.onnx)
```

## 3. Sample

```
$ json2onnx --json_path aaa.json --model_path aaa.onnx
```

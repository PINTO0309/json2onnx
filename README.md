# json2onnx
Converts a JSON file to an ONNX file. Click here for **[onnx2json](https://github.com/PINTO0309/onnx2json)**.

https://github.com/PINTO0309/simple-onnx-processing-tools

[![PyPI - Downloads](https://img.shields.io/pypi/dm/json2onnx?color=2BAF2B&label=Downloads%EF%BC%8FInstalled)](https://pypistats.org/packages/json2onnx) ![GitHub](https://img.shields.io/github/license/PINTO0309/json2onnx?color=2BAF2B) [![PyPI](https://img.shields.io/pypi/v/json2onnx?color=2BAF2B)](https://pypi.org/project/json2onnx/)

<p align="center">
  <img src="https://user-images.githubusercontent.com/33194443/170163032-14b9f769-6f71-41b7-a67b-db168cff949e.png" />
</p>

## 1. Setup
### 1-1. HostPC
```bash
### option
$ echo export PATH="~/.local/bin:$PATH" >> ~/.bashrc \
&& source ~/.bashrc

### run
$ pip install -U onnx protobuf \
&& python3 -m pip install -U onnx_graphsurgeon --index-url https://pypi.ngc.nvidia.com \
&& pip install -U json2onnx
```
### 1-2. Docker
https://github.com/PINTO0309/simple-onnx-processing-tools#docker

## 2. CLI Usage
```
usage:
  json2onnx [-h]
  --ij INPUT_JSON_PATH
  -of OUTPUT_ONNX_FILE_PATH

optional arguments:
  -h, --help
      show this help message and exit

  -ij INPUT_JSON_PATH, --input_json_path INPUT_JSON_PATH
      Input JSON file path (*.json)

  -of OUTPUT_ONNX_FILE_PATH, --output_onnx_file_path OUTPUT_ONNX_FILE_PATH
      Output ONNX model path (*.onnx)
```

## 3. In-script Usage
```python
>>> from json2onnx import convert
>>> help(convert)

Help on function convert in module json2onnx.json2onnx:

convert(
  input_json_path: Union[str, NoneType] = '',
  json_dict: Union[dict, NoneType] = None,
  output_onnx_file_path: Union[str, NoneType] = ''
)

    Parameters
    ----------
    input_json_path: Optional[str]
        Input onnx file path.
        Either input_json_path or json_dict must be specified.
        Default: ''

    json_dict: Optional[dict]
        onnx.ModelProto.
        Either input_onnx_file_path or json_dict must be specified.
        json_dict If specified, ignore input_json_path and process json_dict.

    output_onnx_file_path: Optional[str]
        Output onnx file path. If not specified, no ONNX file is output.
        Default: ''

    Returns
    -------
    onnx_graph: onnx.ModelProto
        Converted ONNX.
```

## 4. CLI Execution
```bash
$ json2onnx \
--input_json_path NonMaxSuppression.json \
--output_onnx_file_path NonMaxSuppression.onnx
```

## 5. In-script Execution
```python
from json2onnx import convert

onnx_graph = convert(
  input_json_path="NonMaxSuppression.json",
  output_onnx_file_path="NonMaxSuppression.onnx",
)

# or

onnx_graph = convert(
  input_json_path="NonMaxSuppression.json",
)

# or

onnx_graph = convert(
  json_dict=json_data,
  output_onnx_file_path="NonMaxSuppression.onnx",
)

# or

onnx_graph = convert(
  json_dict=json_data,
)
```

## 6. Issues
https://github.com/PINTO0309/simple-onnx-processing-tools/issues

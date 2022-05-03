#! /usr/bin/env python

import sys
import onnx
import json
from google.protobuf.json_format import Parse
from typing import Optional
from argparse import ArgumentParser

class Color:
    BLACK          = '\033[30m'
    RED            = '\033[31m'
    GREEN          = '\033[32m'
    YELLOW         = '\033[33m'
    BLUE           = '\033[34m'
    MAGENTA        = '\033[35m'
    CYAN           = '\033[36m'
    WHITE          = '\033[37m'
    COLOR_DEFAULT  = '\033[39m'
    BOLD           = '\033[1m'
    UNDERLINE      = '\033[4m'
    INVISIBLE      = '\033[08m'
    REVERCE        = '\033[07m'
    BG_BLACK       = '\033[40m'
    BG_RED         = '\033[41m'
    BG_GREEN       = '\033[42m'
    BG_YELLOW      = '\033[43m'
    BG_BLUE        = '\033[44m'
    BG_MAGENTA     = '\033[45m'
    BG_CYAN        = '\033[46m'
    BG_WHITE       = '\033[47m'
    BG_DEFAULT     = '\033[49m'
    RESET          = '\033[0m'


def convert(
    input_json_path: Optional[str] = '',
    json_dict: Optional[dict] = None,
    output_onnx_file_path: Optional[str] = '',
):
    """
    Parameters
    ----------
    input_json_path: Optional[str]
        Input onnx file path.\n\
        Either input_json_path or json_dict must be specified.\n\
        Default: ''

    json_dict: Optional[dict]
        onnx.ModelProto.\n\
        Either input_onnx_file_path or json_dict must be specified.\n\
        json_dict If specified, ignore input_json_path and process json_dict.

    output_onnx_file_path: Optional[str]
        Output onnx file path. If not specified, no ONNX file is output.\n\
        Default: ''

    Returns
    -------
    onnx_graph: onnx.ModelProto
        Converted ONNX.
    """

    # Unspecified check for input_onnx_file_path and onnx_graph
    if not input_json_path and not json_dict:
        print(
            f'{Color.RED}ERROR:{Color.RESET} '+
            f'One of input_json_path or json_dict must be specified.'
        )
        sys.exit(1)

    json_file = json_dict
    if not json_dict:
        with open(input_json_path, 'r') as f:
            json_file = json.load(f)

    # Convert JSON to onnx model
    onnx_str = json.dumps(json_file)
    onnx_graph = Parse(onnx_str, onnx.ModelProto())

    if output_onnx_file_path:
        onnx.save(onnx_graph, output_onnx_file_path)

    return onnx_graph


def main():
    parser = ArgumentParser()
    parser.add_argument(
        '--input_json_path',
        type=str,
        required=True,
        help='Input JSON file path (*.json)'
    )
    parser.add_argument(
        '--output_onnx_file_path',
        type=str,
        required=True,
        help='Output ONNX model path (*.onnx)'
    )
    args = parser.parse_args()

    input_json_path = args.input_json_path
    output_onnx_file_path = args.output_onnx_file_path

    onnx_graph = convert(
        input_json_path=input_json_path,
        json_dict=None,
        output_onnx_file_path=output_onnx_file_path,
    )


if __name__ == '__main__':
    main()
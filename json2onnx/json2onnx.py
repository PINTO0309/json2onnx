#! /usr/bin/env python

import onnx
import json
from google.protobuf.json_format import Parse
import os
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--json_path', type=str, required=True, help='Input JSON file path (*.json)')
    parser.add_argument('--model_path', type=str, default='', help='Output ONNX model path (*.onnx)')
    args = parser.parse_args()

    # Convert JSON to onnx model
    json_file_path, json_ext = os.path.splitext(args.json_path)
    json_file = None
    with open(args.json_path, 'r') as f:
        json_file = json.load(f)
    onnx_str = json.dumps(json_file)
    onnx_model = Parse(onnx_str, onnx.ModelProto())

    output_onnx_path = ''
    if args.model_path:
        output_onnx_path = args.model_path
    else:
        output_onnx_path = f'{json_file_path}.onnx'

    onnx.save(onnx_model, output_onnx_path)

if __name__ == '__main__':
    main()

from setuptools import setup, find_packages
from os import path
import re

package_name="json2onnx"
root_dir = path.abspath(path.dirname(__file__))

with open("README.md") as f:
    long_description = f.read()

with open(path.join(root_dir, package_name, '__init__.py')) as f:
    init_text = f.read()
    version = re.search(r'__version__\s*=\s*[\'\"](.+?)[\'\"]', init_text).group(1)

setup(
    name=package_name,
    version=version,
    description=\
        "Converts a JSON file to an ONNX file.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Katsuya Hyodo",
    author_email="rmsdh122@yahoo.co.jp",
    url="https://github.com/PINTO0309/json2onnx",
    license="MIT License",
    packages=find_packages(),
    platforms=["linux", "unix"],
    python_requires=">=3.6",
    entry_points={
        'console_scripts': [
            "json2onnx=json2onnx:main"
        ]
    }
)

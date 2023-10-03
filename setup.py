from glob import glob
from os.path import join, dirname
from setuptools import find_packages, setup

setup(
    name='pyverilog',
    version='0.1',
    packages=find_packages(include=['pyverilog', 'pyverilog.*']),
    install_requires=['PyYAML', 'pyparsing'],
    long_description=open(join(dirname(__file__), 'README.md')).read(),
    long_description_content_type="text/markdown",
    description='Python-based Verilog Parser (currently Netlist only)',
)

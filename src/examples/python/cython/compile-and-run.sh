#!/bin/bash

python3 -m pip install Cython
python3 setup.py build_ext --inplace

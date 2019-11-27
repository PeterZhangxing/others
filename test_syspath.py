#!/usr/bin/python3.5

import os,sys

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(base_dir)
sys.path.append(base_dir)
print(sys.path)


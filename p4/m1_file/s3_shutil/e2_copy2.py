"""
Python Course - Part 4

https://github.com/egalli64/pyco

Module 1 - File

The module shutil: copy2
"""

import shutil

try:
    shutil.copy2("/tmp/hello.txt", "/tmp/ciao.txt")
except FileNotFoundError as ex:
    print("Can't copy2:", ex)

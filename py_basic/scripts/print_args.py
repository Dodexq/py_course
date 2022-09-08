#!/usr/bin/env python3

import sys

print("Program path", sys.argv[0])
for n, arg in enumerate(sys.argv[1:],1):
    print("arg", n, arg)
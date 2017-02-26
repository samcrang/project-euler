#!/usr/bin/env python3

import sys
import importlib

print(importlib.import_module(
    "euler.solution_%s" % sys.argv[1]
).solution())

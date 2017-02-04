#!/usr/bin/env python3

import sys
import importlib

print(importlib.import_module(
    "euler.%s.solution" % sys.argv[1]
).solution())

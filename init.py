#!/usr/bin/env python3

import os
import re

highest = max((int(d) for d in os.listdir('.') if os.path.isdir(
    os.path.join('.', d)) and re.match(r'^\d+', d)), default=None) + 1

os.mkdir(f"{highest}")

with open(f"{highest}/{highest}.py", "w") as f:
    f.write("import sys\n\n")
    f.write(
        "lines = [line.strip() for line in sys.stdin.read().strip().splitlines()]\n")
open(f"{highest}/file.in", "w").close()
open(f"{highest}/sample.in", "w").close()

#!/usr/bin/env python3

import os
import re

highest = max((int(d) for d in os.listdir('.') if os.path.isdir(
    os.path.join('.', d)) and re.match(r'^\d+', d)), default=None) + 1

os.mkdir(f"{highest}")
open(f"{highest}/{highest}.py", "w").close()
open(f"{highest}/file.in", "w").close()
open(f"{highest}/sample.in", "w").close()

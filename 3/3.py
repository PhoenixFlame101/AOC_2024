import sys
import re

part_1 = 0
part_2 = 0

enabled = True
for a, b, do, dont in re.findall(r"mul\((\d{1,3}),(\d{1,3})\)|(do\(\))|(don't\(\))", sys.stdin.read()):
    if do or dont:
        enabled = bool(do)
    else:
        part_1 += int(a)*int(b)
        part_2 += int(a)*int(b)*enabled

# Part 1
print(part_1)

# Part 2
print(part_2)

import sys
from functools import cmp_to_key

rules, updates = sys.stdin.read().split('\n\n')
cmp = cmp_to_key(lambda x, y: 1-2*(f'{x}|{y}' in rules))

part_1 = 0
part_2 = 0
for line in map(lambda x: x.split(','), updates.split()):
    fixed = sorted(line, key=cmp)

    # Part 1
    if line == fixed:
        part_1 += int(fixed[len(fixed)//2])

    # Part 2
    if line != fixed:
        part_2 += int(fixed[len(fixed)//2])

print(part_1)
print(part_2)

import sys
import re


def parse(group):
    for i in range(3):
        match = re.search(r'X.(\d+), Y.(\d+)', group[i])
        group[i] = (int(match.group(1)), int(match.group(2)))
    return group


def solve(group, part_2=False):
    ax, ay = group[0]
    bx, by = group[1]
    tx, ty = (ele + (10000000000000*part_2) for ele in group[2])
    b = (tx*ay-ty*ax)//(ay*bx-by*ax)
    a = (tx*by-ty*bx)//(by*ax-bx*ay)
    if ax*a+bx*b == tx and ay*a+by*b == ty:
        return 3*a+b
    return 0


groups = [parse(line.strip().splitlines())
          for line in sys.stdin.read().strip().split('\n\n')]

# Part 1
print(sum(solve(group) for group in groups))

# Part 2
print(sum(solve(group, True) for group in groups))

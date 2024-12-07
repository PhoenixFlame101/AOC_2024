import sys
import itertools
from functools import reduce

equations = sys.stdin.read().strip().split('\n')
equations = [(int(a.split(':')[0].strip()), tuple(
    map(int, a.split(':')[1].split()))) for a in equations]


def evaluate(x, y, op):
    if op == '+':
        return x+y
    elif op == '*':
        return x*y
    return int(str(x)+str(y))


def can_be_made(target, nums, ops):
    for operators in itertools.product(ops, repeat=len(nums)-1):
        op = iter(operators)
        res = reduce(
            lambda x, y: evaluate(x, y, next(op)), nums)

        if res == target:
            return True


part_1 = 0
part_2 = 0
visited = set()

# Part 1
for eq in equations:
    if can_be_made(eq[0], eq[1], '+*'):
        part_1 += eq[0]
        visited.add(eq)
print(part_1)

# Part 2
part_2 = part_1
for eq in equations:
    if eq not in visited:
        if can_be_made(eq[0], eq[1], '+*|'):
            part_2 += eq[0]
            visited.add(eq)
print(part_2)

import sys
from functools import cache

towels, targets = [line.strip()
                   for line in sys.stdin.read().strip().split('\n\n')]
towels = towels.split(', ')
targets = targets.splitlines()


@cache
def matches(target, part_2=False):
    if not target:
        return 1
    aggregate = sum if part_2 else any
    return aggregate(matches(target[len(towel):], True) for towel in towels if target.startswith(towel))


# Part 1
print(sum(matches(target) for target in targets))

# Part 2
print(sum(matches(target, True) for target in targets))

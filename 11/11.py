import functools
import math
import sys


@functools.cache
def count(x, d):
    if d == 0:
        return 1
    if x == 0:
        return count(1, d-1)

    l = math.floor(math.log10(x))+1

    # Odd number of digits
    if l % 2:
        return count(x*2024, d-1)

    return (count(x // 10**(l//2), d-1) +
            count(x % 10**(l//2), d-1))


stones = list(map(int, sys.stdin.read().strip().split()))

# Part 1
print(sum(map(lambda x: count(x, 25), stones)))

# Part 2
print(sum(map(lambda x: count(x, 75), stones)))

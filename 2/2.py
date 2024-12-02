import sys


def is_ok(elements):
    delta = [b - a for a, b in zip(elements, elements[1:])]
    return all(-3 <= n <= -1 for n in delta) or all(1 <= n <= 3 for n in delta)


part_1 = 0
part_2 = 0
for line in sys.stdin:
    elements = list(map(int, line.split()))
    part_1 += is_ok(elements)
    part_2 += any(is_ok(elements[:i]+elements[i+1:])
                  for i in range(len(elements)))

# Part 1
print(part_1)

# Part 2
print(part_2)

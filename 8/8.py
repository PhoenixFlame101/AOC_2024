import sys
from collections import defaultdict
import itertools

grid = [line.strip() for line in sys.stdin.readlines()]

ele_pos = defaultdict(list)
for i, row in enumerate(grid):
    for j, ele in enumerate(row):
        if ele in '.#':
            continue
        ele_pos[ele].append(complex(i, j))


def is_in_bounds(coords, grid):
    if (coords.real >= 0 and coords.real < len(grid) and
            coords.imag >= 0 and coords.imag < len(grid[0])):
        return True
    return False


def get_antinodes(perm, grid, part):
    anodes = set()
    anode = complex(2*perm[1].real - perm[0].real,
                    2*perm[1].imag - perm[0].imag)

    # Part 1 (only first occurrence)
    if part == 1:
        return {anode} if is_in_bounds(anode, grid) else set()

    # Part 2
    anodes.add(perm[1])
    while is_in_bounds(anode, grid):
        anodes.add(anode)
        anode += complex(perm[1].real - perm[0].real,
                         perm[1].imag - perm[0].imag)

    return anodes


part_1 = set()
part_2 = set()
for ele, pos in ele_pos.items():
    for perm in itertools.permutations(pos, 2):
        part_1 |= get_antinodes(perm, grid, 1)
        part_2 |= get_antinodes(perm, grid, 2)

print(len(part_1))
print(len(part_2))

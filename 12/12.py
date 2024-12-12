import sys
from operator import mul

lines = [line.strip() for line in sys.stdin.readlines()]
n, m = len(lines), len(lines[0])
garden = {i + j * 1j: c for i,
          r in enumerate(lines) for j, c in enumerate(r)}

for i in range(-1, n + 1):
    garden[i - 1 * 1j] = garden[i + m * 1j] = "#"
for j in range(-1, m + 1):
    garden[-1 + j * 1j] = garden[n + j * 1j] = "#"
visited = set()


def dfs(visited, pos, plant, dir):
    if garden[pos] != plant:
        if garden[pos + dir * 1j] == plant or garden[pos - dir + dir * 1j] != plant:
            return 0, 1, 1
        else:
            return 0, 1, 0
    if pos in visited:
        return 0, 0, 0
    visited.add(pos)
    area, perimeter, sides = 1, 0, 0
    for d in (1, -1, 1j, -1j):
        a, p, s = dfs(visited, pos + d, plant, d)
        area, perimeter, sides = area + a, perimeter + p, sides + s
    return area, perimeter, sides


part_1 = 0
part_2 = 0
for pos in garden:
    if pos not in visited and garden[pos] != "#":
        area, perimeter, sides = dfs(visited, pos, garden[pos], 1)
        part_1 += area * perimeter
        part_2 += area * sides

print(part_1)
print(part_2)

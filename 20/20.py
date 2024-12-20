from itertools import combinations
import sys

grid = {i+j*1j: c for i, r in enumerate(sys.stdin)
        for j, c in enumerate(r) if c != '#'}
start, = (p for p in grid if grid[p] == 'S')

distances = {start: 0}
path = [start]

for cur in path:
    for new in cur-1, cur+1, cur-1j, cur+1j:
        if new in grid and new not in distances:
            distances[new] = distances[cur] + 1
            path.append(new)

part_1 = part_2 = 0
for (a, i), (b, j) in combinations(distances.items(), 2):
    dist = abs((a-b).real) + abs((a-b).imag)
    # Part 1
    if dist == 2 and j-i-dist >= 100:
        part_1 += 1
    # Part 2
    if dist <= 20 and j-i-dist >= 100:
        part_2 += 1

print(part_1)
print(part_2)

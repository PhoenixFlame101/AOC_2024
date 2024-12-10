import sys


def flood_fill(grid, visited, i, j, cur=0):
    if (i < 0 or i > len(grid) - 1):
        return 0

    if (j < 0 or j > len(grid[0]) - 1):
        return 0

    if (grid[i][j] != cur):
        return 0

    if cur == 9:
        visited.add((i, j))
        return 1

    count = 0
    count += flood_fill(grid, visited, i-1, j, cur+1)
    count += flood_fill(grid, visited, i+1, j, cur+1)
    count += flood_fill(grid, visited, i, j-1, cur+1)
    count += flood_fill(grid, visited, i, j+1, cur+1)

    return count


lava_map = tuple(list(map(int, line.strip()))
                 for line in sys.stdin.readlines())
trailheads = ((i, j) for i, row in enumerate(lava_map)
              for j, ele in enumerate(row) if ele == 0)

part_1 = 0
part_2 = 0
for t in trailheads:
    visited = set()
    part_2 += flood_fill(lava_map, visited, int(t[0]), int(t[1]))
    part_1 += len(visited)

print(part_1)
print(part_2)

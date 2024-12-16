import sys
import networkx as nx

grid = [line.strip() for line in sys.stdin.read().strip().splitlines()]
print(grid)

directions = (1, -1, 1j, -1j)

graph = nx.DiGraph()
for i, row in enumerate(grid):
    for j, ele in enumerate(row):
        if ele == "#":
            continue

        z = i + 1j * j
        if ele == "S":
            start = (z, 1j)
        if ele == "E":
            end = z
        for dz in directions:
            graph.add_node((z, dz))

for z, dz in graph.nodes:
    if (z + dz, dz) in graph.nodes:
        graph.add_edge((z, dz), (z + dz, dz), score=1)
    for rot in -1j, 1j:
        graph.add_edge((z, dz), (z, dz * rot), score=1000)

for dz in directions:
    graph.add_edge((end, dz), "end", score=0)

# Part 1
print(nx.shortest_path_length(graph, start, "end", "score"))

# Part2
print(len({z for path in nx.all_shortest_paths(
    graph, start, "end", "score") for z, _ in path[:-1]}))

import sys
import networkx as nx


def find_shortest_path(obstacles, limit=1024, end=70):
    n = end + 1
    G = nx.grid_2d_graph(n, n)
    [G.remove_node(obstacle)
     for obstacle in obstacles[:limit] if obstacle in G]

    try:
        return nx.shortest_path(G, source=(0, 0), target=(end, end))
    except nx.NetworkXNoPath:
        return None


obstacles = [tuple(map(int, line.strip().split(',')))
             for line in sys.stdin.read().strip().splitlines()]

# Part 1
print(len(find_shortest_path(obstacles))-1)  # Remove starting node

# Part 2
low = 0
high = len(obstacles)
mid = 0
while low <= high:
    mid = (high + low) // 2
    shortest_path = find_shortest_path(obstacles, mid)
    if shortest_path:
        low = mid + 1
    else:
        high = mid - 1
print(','.join(map(str, obstacles[mid])))

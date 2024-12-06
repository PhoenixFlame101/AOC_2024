import sys

room = {i+j*1j: col for i, row in enumerate(sys.stdin)
        for j, col in enumerate(row.strip())}
start = min(p for p in room if room[p] == '^')


def move_guard(room):
    pos, dir, visited = start, -1, set()
    while pos in room and (pos, dir) not in visited:
        visited.add((pos, dir))
        if room.get(pos+dir) == "#":
            dir *= -1j
        else:
            pos += dir
    # Path, is_cycle
    return {p for p, _ in visited}, (pos, dir) in visited


path = move_guard(room)[0]

# Part 1
print(len(path))

# Part 2
print(sum(move_guard(room | {obstacle_pos: '#'})[1] for obstacle_pos in path))

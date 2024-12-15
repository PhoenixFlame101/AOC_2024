import sys

grid_1, moves = sys.stdin.read().strip().split('\n\n')
grid_2 = grid_1.replace('#', '##').replace(
    '.', '..').replace('O', '[]').replace('@', '@.')

for grid in grid_1, grid_2:
    grid = {i+j*1j: c for j, r in enumerate(grid.split())
            for i, c in enumerate(r)}

    pos = [x for x in grid if grid[x] == '@'][0]

    for move in moves.replace('\n', ''):
        directions = {'<': -1, '>': +1, '^': -1j, 'v': +1j}[move]
        swaps = []
        todo = [pos]
        for task in todo:
            if grid[task] == '#':
                break
            if grid[task] == '.':
                continue
            task += directions
            swaps += [task]
            todo += [task]
            if directions.imag and grid[task] == '[':
                todo += [task+1]
            if directions.imag and grid[task] == ']':
                todo += [task-1]

        else:
            done = set()
            for swap in swaps[::-1]:
                if swap in done:
                    continue
                done.add(swap)
                grid[swap], grid[swap-directions] = grid[swap -
                                                         directions], grid[swap]
            pos += directions

    ans = sum(pos for pos in grid if grid[pos] in 'O[')
    print(int(ans.real + ans.imag*100))

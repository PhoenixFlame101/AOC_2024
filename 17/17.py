import sys
import re


def solve(a, b, c, ops):
    pc = 0
    output = []

    while pc < len(ops):
        C = [0, 1, 2, 3, a, b, c]

        match ops[pc:pc+2]:
            case 0, op: a >>= C[op]
            case 1, op: b ^= op
            case 2, op: b = 7 & C[op]
            case 3, op: pc = op-2 if a else pc
            case 4, op: b ^= c
            case 5, op: output += [C[op] & 7]
            case 6, op: b = a >> C[op]
            case 7, op: c = a >> C[op]
        pc += 2
    return output


a, b, c, *ops = map(int, re.findall(r'\d+', sys.stdin.read()))

# Part 1
print(*solve(a, b, c, ops), sep=',')

# Part 2
stack = [(0, 0)]
part_2 = 0
while stack:
    cur, i = stack.pop()
    if solve(cur, b, c, ops) == ops:
        part_2 = cur
    if solve(cur, b, c, ops) == ops[-i:] or not i:
        for n in range(8):
            stack.append((8*cur+n, i+1))

print(part_2)

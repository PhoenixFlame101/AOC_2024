import sys
data = sys.stdin.read().strip()


def calc(memory):
    for i in range(len(memory))[::-1]:
        for j in range(i):
            i_data, i_size = memory[i]
            j_data, j_size = memory[j]

            if i_data and not j_data and i_size <= j_size:
                memory[i] = (0, i_size)
                memory[j] = (0, j_size - i_size)
                memory.insert(j, (i_data, i_size))

    def flatten(x): return [x for x in x for x in x]

    print(sum(i*(c-1) for i, c in enumerate(flatten(
        [d]*s for d, s in memory)) if c))


# Part 1
part_1 = [(i//2+1 if i % 2 else 0, 1)
          for i, d in enumerate(data, 1) for _ in range(int(d))]
calc(part_1)

# Part 2
part_2 = [(i//2+1 if i % 2 else 0, int(d)) for i, d in enumerate(data, 1)]
calc(part_2)

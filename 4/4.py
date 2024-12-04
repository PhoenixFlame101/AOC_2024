import sys


grid = list(map(lambda x: x.strip(), sys.stdin.readlines()))
part_1_word = "XMAS"
part_2_word = "MAS"

rows = len(grid)
cols = len(grid[0])
word_len = len(part_1_word)
word_len_mid = len(part_2_word)//2
directions = [
    (0, 1),
    (1, 0),
    (0, -1),
    (-1, 0),
    (1, 1),
    (1, -1),
    (-1, 1),
    (-1, -1)
]

part_1 = 0
part_2 = 0

for r in range(rows):
    for c in range(cols):
        # Part 1
        for dr, dc in directions:
            if 0 <= r + (word_len - 1) * dr < rows and 0 <= c + (word_len - 1) * dc < cols:
                if ''.join(grid[r + i * dr][c + i * dc] for i in range(word_len)) == part_1_word:
                    part_1 += 1

        # Part 2
        if (0 <= r - (word_len_mid) < r + (word_len_mid) < rows and
                0 <= c - (word_len_mid) < c + (word_len_mid) < cols):
            found_1 = ''.join(grid[r-word_len_mid+i][c-word_len_mid+i]
                              for i in range(len(part_2_word)))
            found_2 = ''.join(grid[r-word_len_mid+i][c+word_len_mid-i]
                              for i in range(len(part_2_word)))
            if ((found_1 == part_2_word or found_1 == part_2_word[::-1]) and
                    (found_2 == part_2_word or found_2 == part_2_word[::-1])):
                part_2 += 1

print(part_1)
print(part_2)

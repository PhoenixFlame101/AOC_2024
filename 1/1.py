import sys
import bisect

left_side, right_side = list(
    zip(*[map(int, line.split()) for line in sys.stdin]))
right_side.sort()

# Part 1
print(sum([abs(left-right)
      for left, right in zip(sorted(left_side), right_side)]))

# Part 2
print(sum([(bisect.bisect_right(right_side, ele) -
      bisect.bisect_left(right_side, ele))*ele for ele in left_side]))

import sys
import re
import math


def parse(line):
    match = re.search(r'p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)', line)
    return [complex(int(match.group(1)), int(match.group(2))), complex(int(match.group(3)), int(match.group(4)))]


def move_robot(pos, vel, limit=(101, 103)):
    new_pos = pos+vel
    return complex(new_pos.real % limit[0], new_pos.imag % limit[1])


def calc_safety_factor(robots, limit=(101, 103)):
    x = limit[0]//2 - 1
    y = limit[1]//2 - 1

    quads = [0 for _ in range(4)]
    for robot in robots:
        robot_pos = robot[0]
        if robot_pos.real <= x and robot_pos.imag <= y:
            quads[0] += 1
        elif robot_pos.real <= x and robot_pos.imag > y + 1:
            quads[1] += 1
        elif robot_pos.real > x+1 and robot_pos.imag <= y:
            quads[2] += 1
        elif robot_pos.real > x+1 and robot_pos.imag > y+1:
            quads[3] += 1

    return math.prod(quads)


robots = [parse(line.strip())
          for line in sys.stdin.read().strip().splitlines()]

num_unique_positions = 0
iteration = 0
while num_unique_positions < len(robots) or iteration <= 100:
    iteration += 1
    robots = [[move_robot(pos, vel), vel] for pos, vel in robots]
    if iteration == 100:
        # Part 1
        print(calc_safety_factor(robots))
    num_unique_positions = len({pos for pos, vel in robots})
else:
    # Part 2
    print(iteration)

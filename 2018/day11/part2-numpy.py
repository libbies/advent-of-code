#!/usr/bin/env python
"""advent of code 2018 day 11 part 2"""
import numpy
serial = int(open("input.txt").read().strip())

def power(x, y, _serial=serial):
    if x >= 300 or y >= 300:
        return 0
    rack_id = x + 10
    power = rack_id * y
    power += _serial or serial
    power *= rack_id
    try:
        power = int(str(power)[-3])
    except IndexError:
        power = 0
    power -= 5
    return power

assert power(3, 5, _serial=8) == 4
assert power(122, 79, _serial=57) == -5
assert power(217, 196, _serial=39) == 0
assert power(101, 153, _serial=71) == 4

grid = numpy.zeros([300,300], dtype=int)
for x in range(300):
    for y in range(300):
        grid[x,y] = power(x,y)

best = 0
for size in range(1, 26): # hax, no need to search full range
    for x in range(300):
        for y in range(300):
            power_level = numpy.sum(grid[x:x+size, y:y+size])
            if power_level > best:
                best = power_level
                answer = f"{x},{y},{size}"
    # print(size, best, answer)

print("aoc 2018 day 11 part 2:", answer)

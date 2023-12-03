#!/usr/bin/env python
"""advent of code 2018 day 11 part 2"""
serial = int(open("input.txt").read().strip())

def power(x, y, _serial=serial):
    rack_id = x + 10
    power = rack_id * y
    power += _serial
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

grid = tuple(tuple(power(x,y) for x in range(300)) for y in range(300))

best = 0
answer = ""
for size in range(1, 26): # hax, no need to search full range
    for x in range(301-size):
        for y in range(301-size):
            power = sum(sum(row[x:x+size]) for row in grid[y:y+size])
            if power > best:
                best = power
                answer = f"{x},{y},{size}"

print("aoc 2018 day 11 part 2:", answer)

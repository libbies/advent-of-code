#!/usr/bin/env python
"""advent of code 2018 day 10 part 2"""
import re
from collections import namedtuple
from pprint import pprint

Point = namedtuple("Point", ("x", "y", "vel_x", "vel_y"))
points = [
        Point._make(map(int, re.findall("[0-9-]+", _)))
        for _ in set(open("input.txt").read().splitlines())
    ]

grid = {}
for p in points:
    grid[p.x,p.y] = [p.x, p.y]

second = 0
while True:
    dist_y = max(y for _, y in grid.values()) - min(y for _, y in grid.values())
    if dist_y <= 9:
        break
    second += 1
    for p in points:
        grid[p.x, p.y][0] += p.vel_x
        grid[p.x, p.y][1] += p.vel_y

print("aoc 2018 day 10 part 2:", second)

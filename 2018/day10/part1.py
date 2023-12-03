#!/usr/bin/env python
"""advent of code 2018 day 10 part 1"""
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
    min_y = min(y for _, y in grid.values())
    max_y = max(y for _, y in grid.values())
    dist_y = max_y - min_y + 1
    if dist_y <= 10:
        break
    second += 1
    for p in points:
        grid[p.x, p.y][0] += p.vel_x
        grid[p.x, p.y][1] += p.vel_y

min_x = min(x for x, _ in grid.values())
max_x = max(x for x, _ in grid.values())
dist_x = max_x - min_x + 1

message = [[" " for x in range(dist_x)] for y in range(dist_y)]
for x,y in grid.values():
    message[y-min_y][x-min_x] = "█"

print("aoc 2018 day 10 part 1:")
for row in message:
    print(''.join(row))

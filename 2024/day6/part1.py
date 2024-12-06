#!/usr/bin/env python3
"""advent of code 2024 day 6 part 1"""
from collections import defaultdict

lines = open("input.txt").read().splitlines()
width = max(len(lines), len(lines[0]))
grid = defaultdict(str)
for x, line in enumerate(lines):
    for y, char in enumerate(line):
        grid[x,y] = char
        if char == '^':
            location = (x,y)

locations = {location}
direction = 0
dirs = ((-1, 0), (0, 1), (1, 0), (0, -1))
while 0 <= location[0] < width and 0 <= location[1] < width:
    x, y = location
    x += dirs[direction][0]
    y += dirs[direction][1]
    if grid[x,y]=='#':
        direction = (direction+1)%4
    else:
        location = (x,y)
        locations.add(location)

answer = len(locations) - 1
print("aoc 2024 day 6 part 1:", answer)

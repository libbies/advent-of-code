#!/usr/bin/env python3
"""advent of code 2024 day 6 part 2"""
from collections import defaultdict

lines = open("input.txt").read().splitlines()
height = len(lines)
width = len(lines[0])
grid = defaultdict(str)
for x, line in enumerate(lines):
    for y, char in enumerate(line):
        grid[x,y] = char
        if char == '^':
            start = (x,y)

dirs = ((-1, 0), (0, 1), (1, 0), (0, -1))
obstructions = list()
for dx in range(height):
    for dy in range(width):
        if grid[dx,dy] in ('#', '^'):
            continue
        tmp = grid.copy()
        tmp[dx,dy] = '#'
        location = start
        locations = {location: [-1]}
        direction = 0
        while 0 <= location[0] < height and 0 <= location[1] < width:
            x, y = location
            x += dirs[direction][0]
            y += dirs[direction][1]
            if tmp[x,y]=='#':
                direction = (direction+1)%4
            else:
                location = (x,y)
                if location in locations:
                    if direction in locations[location]:
                        # loop detected
                        obstructions.append((dx,dy))
                        break
                    locations[x,y].append(direction)
                else:
                    locations[x,y] = [direction]

answer = len(obstructions)
print("aoc 2024 day 6 part 2:", answer)

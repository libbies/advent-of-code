#!/usr/bin/env python3
"""advent of code 2024 day 18 part 2"""
from collections import defaultdict

lines = open("input.txt").read().splitlines()
answer = 0

height = max(int(line.split(',')[1]) for line in lines for y in line.split(','))
width = max(int(line.split(',')[0]) for line in lines for y in line.split(','))
bounds = set()
limit = height*width
for n in range(len(lines)):
    grid = defaultdict(lambda: 2**31)
    for i, line in enumerate(lines):
        if i>=n:
            break
        x, y = map(int, line.split(','))
        if (x,y) in grid:
            continue
        grid[x,y] = '#'
        bounds.add((x,y))
        answer = (x,y)
    grid[0,0] = 0
    counter = 0
    while grid[width,height] == 2**31:
        counter += 1
        if counter>=limit:
            break
        for x in range(width+1):
            for y in range(height+1):
                for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
                    if (x,y) in bounds:
                        continue
                    if (x+dx,y+dy) in bounds:
                        continue
                    if grid[x+dx,y+dy] >= grid[x,y]+1:
                        grid[x+dx,y+dy] = grid[x,y]+1
    else:
        continue
    break

print("aoc 2024 day 18 part 2:", answer)

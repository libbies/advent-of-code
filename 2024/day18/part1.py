#!/usr/bin/env python3
"""advent of code 2024 day 18 part 1"""
from collections import defaultdict

lines = open("input.txt").read().splitlines()
answer = 0

grid = defaultdict(lambda: 2**32)
height = max(int(line.split(',')[-1]) for line in lines for y in line.split(','))
width = max(int(line.split(',')[-1]) for line in lines for y in line.split(','))
bounds = set()
for i, line in enumerate(lines):
    if i>=1024:
        break
    x, y = map(int, line.split(','))
    width = max(width, x)
    grid[x,y] = '#'
    bounds.add((x,y))

grid[0,0] = 0
while grid[width,height] == 2**32:
    for x in range(width+1):
        for y in range(height+1):
            for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
                if (x,y) in bounds or (x+dx,y+dy) in bounds:
                    continue
                if grid[x+dx,y+dy] >= grid[x,y]+1:
                    grid[x+dx,y+dy] = grid[x,y]+1

answer = grid[width,height]
print("aoc 2024 day 18 part 1:", answer)

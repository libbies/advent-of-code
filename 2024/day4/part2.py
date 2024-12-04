#!/usr/bin/env python3
"""advent of code 2024 day 4 part 2"""
from collections import defaultdict

lines = open("input.txt").read().splitlines()
width = max(len(lines), len(lines[0]))
grid = defaultdict(str)
for x, line in enumerate(lines):
    for y, char in enumerate(line):
        grid[x,y] = char

answer = 0
for x in range(width):
    for y in range(width):
        if grid[x+1,y+1]=="A" and ((grid[x,y]=="M" and grid[x+2,y+2]=="S")
                                or (grid[x,y]=="S" and grid[x+2,y+2]=="M")):
            if ((grid[x+2,y]=="M" and grid[x,y+2]=="S")
                    or (grid[x+2,y]=="S" and grid[x,y+2]=="M")):
                answer += 1

print("aoc 2024 day 4 part 2:", answer)

#!/usr/bin/env python3
"""advent of code 2024 day 4 part 1"""
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
        if grid[x,y]=="X":
            if grid[x+1,y]=="M" and grid[x+2,y]=="A" and grid[x+3,y]=="S":
                answer += 1
            if grid[x,y+1]=="M" and grid[x,y+2]=="A" and grid[x,y+3]=="S":
                answer += 1
            if grid[x+1,y+1]=="M" and grid[x+2,y+2]=="A" and grid[x+3,y+3]=="S":
                answer += 1
            if grid[x+1,y-1]=="M" and grid[x+2,y-2]=="A" and grid[x+3,y-3]=="S":
                answer += 1
        if grid[x,y]=="S":
            if grid[x+1,y]=="A" and grid[x+2,y]=="M" and grid[x+3,y]=="X":
                answer += 1
            if grid[x,y+1]=="A" and grid[x,y+2]=="M" and grid[x,y+3]=="X":
                answer += 1
            if grid[x+1,y+1]=="A" and grid[x+2,y+2]=="M" and grid[x+3,y+3]=="X":
                answer += 1
            if grid[x+1,y-1]=="A" and grid[x+2,y-2]=="M" and grid[x+3,y-3]=="X":
                answer += 1

print("aoc 2024 day 4 part 1:", answer)

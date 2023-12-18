#!/usr/bin/env python
"""advent of code 2023 day 18 part 1"""
from collections import defaultdict, deque
lines = [l.split() for l in open("input.txt").readlines()]

digs = defaultdict(str)
row, col = 0, 0
for direction, distance, color in lines:
    distance = int(distance)
    if direction == "U":
        for n in range(distance):
            digs[row-n,col] = color
        row -= distance
    if direction == "D":
        for n in range(distance):
            digs[row+n,col] = color
        row += distance
    if direction == "L":
        for n in range(distance):
            digs[row,col-n] = color
        col -= distance
    if direction == "R":
        for n in range(distance):
            digs[row,col+n] = color
        col += distance

min_row = min(row for (row,col) in digs.keys())
min_col = min(col for (row,col) in digs.keys())
max_row = max(row for (row,col) in digs.keys())
max_col = max(col for (row,col) in digs.keys())

grid = [['.'] * (3+max_col-min_col) for n in range(3+max_row-min_row)]
for row, col in digs:
    grid[1+row-min_row][1+col-min_col] = '#'

max_row = len(grid)
max_col = len(grid[0])
queue = deque()
queue.append((0,0))
while queue:
    row, col = queue.pop()
    grid[row][col] = ' '
    for x, y in ((1,0), (-1,0), (0,1), (0,-1)):
        if row+x<0 or row+x>=max_row:
            continue
        if col+y<0 or col+y>=max_col:
            continue
        if grid[row+x][col+y]=='.':
            queue.append((row+x, col+y))

answer = sum(row.count('#') for row in grid) + sum(row.count('.') for row in grid)
print("aoc 2023 day 18 part 1:", answer)

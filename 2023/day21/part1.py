#!/usr/bin/env python
"""advent of code 2023 day 21 part 1"""
lines = [list(l.strip()) for l in open("input.txt").readlines()]

maxlen = len(lines)

steps = [[0] * maxlen for _ in range(maxlen)]

for row, line in enumerate(lines):
    if 'S' not in line:
        continue
    start = (row, line.index('S'))
    break

queue = [start]
goal = 64
for n in range(goal):
    tmp = []
    for (row, col) in queue:
        for dx, dy in ((0, 1), (1,0), (-1,0), (0,-1)):
            if not (0<=row+dx<maxlen and 0<=col+dy<maxlen):
                continue
            if lines[row+dx][col+dy] == '#':
                continue
            if steps[row+dx][col+dy] != 0:
                continue
            steps[row+dx][col+dy] = n+1
            tmp.append((row+dx,col+dy))
    queue = tmp

answer = sum(sum(1 for step in row if step and step%2==0) for row in steps)
print("aoc 2023 day 21 part 1:", answer)

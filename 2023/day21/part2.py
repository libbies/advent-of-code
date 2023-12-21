#!/usr/bin/env python
"""advent of code 2023 day 21 part 2"""
from collections import deque
from itertools import pairwise
lines = [list(l.strip()) for l in open("input.txt").readlines()]

maxlen = len(lines)
for row, line in enumerate(lines):
    if 'S' not in line:
        continue
    start = (row, line.index('S'))
    break

queue = [start]
goal = 26501365
counts = list()
n, steps = 0, 0
visited = set()
while len(counts)!=3:
    tmp = deque()
    for (row, col) in queue:
        for dx, dy in ((0, 1), (1,0), (-1,0), (0,-1)):
            if lines[(row+dx)%maxlen][(col+dy)%maxlen] == '#':
                continue
            if (row+dx,col+dy) in visited:
                continue
            visited.add((row+dx,col+dy))
            if n%2==0:
                steps += 1
            tmp.append((row+dx,col+dy))
    queue = tmp
    if n%(maxlen*2)==goal%maxlen:
        counts.append(steps)
    n += 1

differences = [a-b for a,b in pairwise(counts[::-1])]
cycle = [a-b for a,b in pairwise(differences)]
assert cycle.count(cycle[-1])==len(cycle)

answer = steps
diff = differences[0]
while n<goal:
    n += maxlen * 2
    diff += cycle[0]
    answer += diff

print("aoc 2023 day 21 part 2:", answer)

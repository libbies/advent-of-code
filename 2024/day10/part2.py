#!/usr/bin/env python3
"""advent of code 2024 day 10 part 2"""
from collections import defaultdict

queue = list()
topograph = defaultdict(int)
for x, line in enumerate(open("input.txt").read().splitlines()):
    for y, height in enumerate(line):
        topograph[x,y] = int(height)
        if height=='0':
            queue.append(((x,y), x, y))

for n in range(1, 10):
    tmp = list()
    for head, x, y in queue:
        for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
            if topograph[x+dx, y+dy]==n:
                tmp.append((head, x+dx, y+dy))
    queue = tmp

answer = len(queue)
print("aoc 2024 day 10 part 2:", answer)

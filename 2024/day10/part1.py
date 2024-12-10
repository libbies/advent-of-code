#!/usr/bin/env python3
"""advent of code 2024 day 10 part 1"""
from collections import defaultdict

queue = set()
topograph = defaultdict(int)
for x, line in enumerate(open("input.txt").read().splitlines()):
    for y, height in enumerate(line):
        topograph[x,y] = int(height)
        if height=='0':
            queue.add(((x,y), x, y))

for n in range(1, 10):
    queue = {
        (head, x+dx, y+dy)
        for head, x, y in queue
        for dx,dy in ((1,0),(-1,0),(0,1),(0,-1))
        if topograph[x+dx, y+dy]==n
    }

answer = len(queue)
print("aoc 2024 day 10 part 1:", answer)

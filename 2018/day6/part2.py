#!/usr/bin/env python
"""advent of code 2018 day 6 part 2"""
from collections import defaultdict
coords = tuple(tuple(map(int, _.split(", "))) for _ in open("input.txt").read().splitlines())

def dist(x, y):
    return sum(abs(x-i) + abs(y-j) for i, j in coords)

limit = 10000
buffer = limit - min(dist(x, y) for x, y in coords)

min_x = min(x - buffer for x, y in coords)
max_x = max(x + buffer for x, y in coords)
min_y = min(y - buffer for x, y in coords)
max_y = max(y + buffer for x, y in coords)

safe = set()
for i in range(min_x, max_x, 1):
    for j in range(min_y, max_y, 1):
        if limit > dist(i, j):
            safe.add((i,j))

answer = len(safe)
print("aoc 2018 day 6 part 2:", answer)

#!/usr/bin/env python
"""advent of code 2018 day 3 part 1"""
import re
claims = [[int(_) for _ in re.split("[^0-9]+", _) if _] for _ in open("input.txt").read().splitlines()]

l = 1000
grid = [[0 for _ in range(l)] for _ in range(l)]
for claim, y, x, w, h in claims:
    for i in range(h):
        for j in range(w):
            grid[x+i][y+j] = grid[x+i][y+j] + 1

answer = sum(sum(1 for _ in grid[i] if _>=2) for i in range(l))
print("aoc 2018 day 3 part 1:", answer)

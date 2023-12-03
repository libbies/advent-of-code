#!/usr/bin/env python
"""advent of code 2018 day 3 part 2"""
import re
claims = [[int(_) for _ in re.split("[^0-9]+", _) if _] for _ in open("input.txt").read().splitlines()]

l = 1000
grid = [[list() for _ in range(l)] for _ in range(l)]
candidates = {c[0] for c in claims}
for claim, y, x, w, h in claims:
    for i in range(h):
        for j in range(w):
            grid[x+i][y+j].append(claim)

for row in grid:
    for c in row:
        if len(c) >= 2:
            for claim in c:
                if claim in candidates:
                    candidates.remove(claim)

answer = candidates.pop()
print("aoc 2018 day 3 part 2:", answer)

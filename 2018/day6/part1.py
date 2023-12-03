#!/usr/bin/env python
"""advent of code 2018 day 6 part 1"""
from collections import defaultdict
coords = tuple(tuple(map(int, _.split(", "))) for _ in open("input.txt").read().splitlines())

limit = max(max(c) for c in coords) // 5 # magic

grid = defaultdict(lambda: None)
for x, y in coords:
    grid[x,y] = (x,y)

done = set()
tmp = grid.copy()
answer = 0
while limit:
    for (x, y), origin in grid.items():
        if (x, y) in done:
            continue
        done.add((x,y))
        if origin == False:
            continue
        for i, j in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            if tmp[x+i,y+j] is None:
                tmp[x+i,y+j] = origin
            elif tmp[x+i,y+j] != origin and (x+i,y+j) not in grid:
                tmp[x+i,y+j] = False
    for coord in coords:
        c = list(tmp.values()).count(coord)
        if c > answer and c == list(grid.values()).count(coord):
            answer = c
    grid = tmp.copy()
    limit -= 1

print("aoc 2018 day 6 part 1:", answer)

#!/usr/bin/env python
"""advent of code 2023 day 22 part 1"""
lines = open("input.txt").readlines()

blocks = list()
for l in lines:
    a, b = l.strip().split('~')
    blocks.append([*map(int, a.split(',')), *map(int, b.split(','))])

drops = []
for ax, ay, az, bx, by, bz in sorted(blocks, key=lambda b:b[2]):
    block = []
    for x in range(ax, bx+1):
        for y in range(ay, by+1):
            for z in range(az, bz+1):
                block.append((x,y,z))
    drops.append(block)

grid = dict()
underneath = list()
for n, block in enumerate(drops):
    for h in range(block[0][-1]+1):
        if any((x,y,z-h-1) in grid or z-h==0 for x,y,z in block):
            # can't go further down
            underneath.append((n, {grid[x,y,z-h-1] for x,y,z in block if (x,y,z-h-1) in grid}))
            for x,y,z in block:
                grid[x,y,z-h] = n
            break

candidates = [*range(len(drops))]
for c in range(len(drops)):
    for (n, under) in underneath:
        if len(under)==1 and c in under:
            candidates.remove(c)
            break

answer = len(candidates)
print("aoc 2023 day 22 part 1:", answer)

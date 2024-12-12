#!/usr/bin/env python3
"""advent of code 2024 day 12 part 2"""
from collections import defaultdict

lines = open("input.txt").read().splitlines()
height = len(lines)
width = len(lines[0])

plots = defaultdict(str)
for x, line in enumerate(lines):
    for y, plant in enumerate(line):
        plots[x,y] = plant

regions = defaultdict(list)
for x in range(height):
    for y in range(width):
        regions[p := plots[x,y]].append({(x,y)})
        for region in regions[p]:
            if (x-1,y) in region:
                region.add((x,y))
            if (x,y-1) in region:
                region.add((x,y))
        if sets := [r for r in regions[p] if (x,y) in r]:
            regions[p] = [set.union(*sets)] + [r for r in regions[p] if (x,y) not in r]

answer = 0
for p in regions:
    for s in regions[p]:
        sides = 0
        for h in range(height):
            candidates = [(x,y) for x,y in s if x==h and (x-1,y) not in s]
            sides += sum(1 for (x,y) in candidates if (x,y-1) not in candidates)
            candidates = [(x,y) for x,y in s if x==h and (x+1,y) not in s]
            sides += sum(1 for (x,y) in candidates if (x,y-1) not in candidates)
        for w in range(width):
            candidates = [(x,y) for x,y in s if y==w and (x,y-1) not in s]
            sides += sum(1 for (x,y) in candidates if (x-1,y) not in candidates)
            candidates = [(x,y) for x,y in s if y==w and (x,y+1) not in s]
            sides += sum(1 for (x,y) in candidates if (x-1,y) not in candidates)
        answer += len(s) * sides

print("aoc 2024 day 12 part 2:", answer)

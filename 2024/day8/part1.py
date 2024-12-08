#!/usr/bin/env python3
"""advent of code 2024 day 8 part 1"""
from collections import defaultdict
from itertools import combinations

lines = open("input.txt").read().splitlines()
height = len(lines)
width = len(lines[0])
frequencies = defaultdict(list)
for x, line in enumerate(lines):
    for y, char in enumerate(line):
        if char =='.':
            continue
        frequencies[char].append((x,y))

nodes = set()
for char in frequencies:
    for (x1,y1), (x2,y2) in combinations(frequencies[char], 2):
        dx, dy = x1-x2, y1-y2
        if 0<=x1+dx<height and 0<=y1+dy<width:
            nodes.add((x1+dx, y1+dy))
        if 0<=x2-dx<height and 0<=y2-dy<width:
            nodes.add((x2-dx, y2-dy))

answer = len(nodes)
print("aoc 2024 day 8 part 1:", answer)

#!/usr/bin/env python3
"""advent of code 2024 day 8 part 2"""
from collections import defaultdict
from itertools import combinations

lines = open("input.txt").read().splitlines()
height = len(lines)
width = len(lines[0])
frequencies = defaultdict(list)
for x, line in enumerate(lines):
    for y, char in enumerate(line):
        if char=='.':
            continue
        frequencies[char].append((x,y))

nodes = set()
for char in frequencies:
    for (x1,y1), (x2,y2) in combinations(frequencies[char], 2):
        nodes.add((x1,y1))
        nodes.add((x2,y2))
        dx, dy = x1-x2, y1-y2
        step = 1
        while 0<=x1+dx*step<height and 0<=y1+dy*step<width:
            nodes.add((x1+dx*step, y1+dy*step))
            step += 1
        step = 1
        while 0<=x2-dx*step<height and 0<=y2-dy*step<width:
            nodes.add((x2-dx*step, y2-dy*step))
            step += 1

answer = len(nodes)
print("aoc 2024 day 8 part 2:", answer)

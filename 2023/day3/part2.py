#!/usr/bin/env python
"""advent of code 2023 day 3 part 2"""
from math import prod
lines = [tuple(l) for l in open("input.txt").read().splitlines()]

max_x, max_y = len(lines), len(lines[0])
numbers = dict()
for i, line in enumerate(lines):
    number, coords = "", []
    for j, c in enumerate(line):
        if not number and c.isnumeric():
            number = c
            coords.append((i,j))
        elif number and c.isnumeric():
            number += c
            coords.append((i,j))
        elif number and not c.isnumeric():
            for x, y in coords:
                numbers[x,y] = int(number)
            number, coords = "", []
    if number:
        for x, y in coords:
            numbers[x,y] = int(number)

answer = 0
for i, line in enumerate(lines):
    for j, c in enumerate(line):
        if c!='*':
            continue
        parts = set()
        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                try:
                    parts.add(numbers[i+dx,j+dy])
                except KeyError:
                    continue
        if len(parts)==2:
            answer += prod(parts)

print("aoc 2023 day 3 part 2:", answer)

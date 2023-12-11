#!/usr/bin/env python
"""advent of code 2023 day 1 part 1"""
from itertools import combinations
lines = open("input.txt").read().splitlines()

universe = list()
empty_rows = list(range(len(lines)))
empty_cols = list(range(len(lines[0])))
for i, row in enumerate(lines):
    row = list(row)
    if i in empty_rows and '#' in row:
        empty_rows.remove(i)
    universe.append(row)
    for j, char in enumerate(row):
        if j in empty_cols and char!=".":
            empty_cols.remove(j)

galaxies = []
for i, row in enumerate(universe):
    for j, char in enumerate(row):
        if char=="#":
            galaxies.append((i,j))

answer = 0
for g1, g2 in combinations(galaxies, 2):
    distance = abs(g1[0]-g2[0]) + abs(g1[-1]-g2[-1])
    for row in empty_rows:
        if (g1[0] < row < g2[0]) or (g2[0] < row < g1[0]):
            distance += 999_999
    for col in empty_cols:
        if (g1[-1] < col < g2[-1]) or (g2[-1] < col < g1[-1]):
            distance += 999_999
    answer += distance

print(answer)

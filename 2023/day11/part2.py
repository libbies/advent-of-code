#!/usr/bin/env python
"""advent of code 2023 day 11 part 2"""
from itertools import combinations
lines = [list(l.strip()) for l in open("input.txt").readlines()]

universe = list()
galaxies = list()
empty_rows = list(range(len(lines)))
empty_cols = list(range(len(lines[0])))
for i, row in enumerate(lines):
    if i in empty_rows and '#' in row:
        empty_rows.remove(i)
    universe.append(row)
    for j, char in enumerate(row):
        if char=='#':
            galaxies.append((i,j))
            if j in empty_cols:
                empty_cols.remove(j)

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

print("aoc 2023 day 11 part 2:", answer)

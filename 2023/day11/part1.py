#!/usr/bin/env python
"""advent of code 2023 day 11 part 1"""
from itertools import combinations
lines = [list(l.strip()) for l in open("input.txt").readlines()]

universe = list()
empty_cols = list(range(len(lines[0])))
for row in lines:
    if '#' not in row:
        universe.append(row.copy())
    universe.append(row)
    for i, char in enumerate(row):
        if i in empty_cols and char!='.':
            empty_cols.remove(i)

for row in universe:
    for j in reversed(empty_cols):
        row.insert(j, '.')

galaxies = []
for i, row in enumerate(universe):
    for j, char in enumerate(row):
        if char=='#':
            galaxies.append((i,j))

answer = 0
for g1, g2 in combinations(galaxies, 2):
    answer += abs(g1[0]-g2[0]) + abs(g1[-1]-g2[-1])

print("aoc 2023 day 11 part 1:", answer)

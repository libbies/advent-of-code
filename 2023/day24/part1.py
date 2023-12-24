#!/usr/bin/env python
"""advent of code 2024 day 24 part 1"""
import re
from itertools import combinations
from sympy import Point, Segment
hail = [[int(_) for _ in re.split(r"[^0-9-]+", l.strip())] for l in open("input.txt").readlines()]

minbound = 200000000000000
maxbound = 400000000000000
lines = list()
for px, py, pz, vx, vy, vz in hail:
    lines.append(Segment(Point(px, py), Point(px+(vx*maxbound), py+(vy*maxbound))))

answer = 0
for s1, s2 in combinations(lines, 2):
    point = s1.intersection(s2)
    if point and minbound<point[0].x<maxbound and minbound<point[0].y<maxbound:
        answer += 1

print("aoc 2023 day 24 part 1:", answer)

#!/usr/bin/env python
"""advent of code 2023 day 2 part 2"""
import re
lines = (re.split("[:;]", l) for l in open("input.txt").readlines())

answer = 0
for line in lines:
    r, g, b = 0, 0, 0
    for games in line[1:]:
        for ball in games.split(", "):
            n, color = ball.split()
            n = int(n)
            if color=="red":
                r = max(n, r)
            if color=="green":
                g = max(n, g)
            if color=="blue":
                b = max(n, b)
    answer += r * g * b

print("aoc 2023 day 2 part 2:", answer)

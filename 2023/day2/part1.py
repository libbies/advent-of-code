#!/usr/bin/env python
"""advent of code 2023 day 2 part 1"""
import re
lines = (re.split("[:;]", l) for l in open("input.txt").readlines())

answer = 0
for line in lines:
    impossible = False
    for game in line[1:]:
        for ball in game.split(", "):
            n, color = ball.split()
            n = int(n)
            if ((color=="red" and n > 12) \
                    or (color=="green" and n > 13) \
                    or (color=="blue" and n > 14)):
                impossible = True
                break
        if impossible:
            break
    if not impossible:
        answer += int(line[0].split()[-1])

print("aoc 2023 day 2 part 1:", answer)

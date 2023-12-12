#!/usr/bin/env python
"""advent of code 2023 day 12 part 1"""
import re
lines = (l.split() for l in open("input.txt").readlines())

answer = 0
for springs, damaged in lines:
    damaged = map(int, damaged.split(','))
    candidates = [""]
    pattern = re.compile(r"^\.*" + r"\.+".join(c * '#' for c in damaged) + r"\.*$")
    for c in springs:
        tmp = []
        if c in ".#":
            for candidate in candidates:
                tmp.append(candidate + c)
        elif c=='?':
            for candidate in candidates:
                tmp.append(candidate + '#')
                tmp.append(candidate + '.')
        candidates = tmp
    for c in candidates:
        if re.search(pattern, c):
            answer += 1

print("aoc 2023 day 12 part 1:", answer)

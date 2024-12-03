#!/usr/bin/env python3
"""advent of code 2024 day 3 part 1"""
import re

lines = open("input.txt").read().splitlines()
answer = 0
for line in lines:
    for match in re.findall(r"mul\([0-9]+,[0-9]+\)", line):
        a, b = map(int, match[4:-1].split(','))
        answer += a*b

print("aoc 2024 day 3 part 1:", answer)

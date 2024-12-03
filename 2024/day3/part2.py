#!/usr/bin/env python3
"""advent of code 2024 day 3 part 2"""
import re

lines = open("input.txt").read().splitlines()
answer = 0
enabled = True
for line in lines:
    for m in re.findall(r"(do\(\)|don\'t\(\)|mul\([0-9]+,[0-9]+\))", line):
        if m == "do()":
            enabled = True
        elif m == "don't()":
            enabled = False
        elif enabled:
            a, b = map(int, m[4:-1].split(','))
            answer += a*b

print("aoc 2024 day 3 part 2:", answer)

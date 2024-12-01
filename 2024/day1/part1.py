#!/usr/bin/env python
"""advent of code 2024 day 1 part 1"""

lines = open("input.txt").read().splitlines()

lefts = sorted(int(_.split()[0]) for _ in lines)
rights = sorted(int(_.split()[1]) for _ in lines)

answer = 0
for i, left in enumerate(lefts):
    answer += abs(left - rights[i])

print("aoc 2024 day 1 part 1:", answer)

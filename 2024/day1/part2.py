#!/usr/bin/env python
"""advent of code 2024 day 1 part 2"""

lines = open("input.txt").read().splitlines()

lefts = sorted(int(_.split()[0]) for _ in lines)
rights = sorted(int(_.split()[1]) for _ in lines)

answer = 0
for left in lefts:
    answer += left * rights.count(left)


print("aoc 2024 day 1 part 2:", answer)

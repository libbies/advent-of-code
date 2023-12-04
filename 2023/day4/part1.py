#!/usr/bin/env python
"""advent of code 2023 day 4 part 1"""
import re
lines = [re.split("( \| |: )", l) for l in open("input.txt").read().splitlines()]

answer = 0
for card, _, numbers, _, winners in lines:
    numbers = [int(_) for _ in numbers.split()]
    winners = [int(_) for _ in winners.split()]
    points = int(2**(sum(1 for c in numbers if c in winners)-1))
    answer += points

print("aoc 2023 day 4 part 1:", answer)

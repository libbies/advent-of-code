#!/usr/bin/env python
"""advent of code 2018 day 2 part 1"""
from collections import Counter
counts = [Counter(_) for _ in open("input.txt").read().splitlines()]

answer = sum(2 in _.values() for _ in counts) * sum(3 in _.values() for _ in counts)
print("aoc 2018 day 2 part 1:", answer)

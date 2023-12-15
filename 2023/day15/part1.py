#!/usr/bin/env python
"""advent of code 2023 day 15 part 1"""
steps = open("input.txt").read().strip().split(',')

answer = 0
for step in steps:
    value = 0
    for c in step:
        value += ord(c)
        value *= 17
        value %= 256
    answer += value

print("aoc 2023 day 15 part 1:", answer)

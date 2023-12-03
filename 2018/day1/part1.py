#!/usr/bin/env python
"""advent of code 2018 day 1 part 1"""
numbers = [int(_) for _ in open("input.txt").read().splitlines()]

answer = sum(numbers)
print("aoc 2018 day 1 part 1:", answer)

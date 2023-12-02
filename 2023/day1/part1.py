#!/usr/bin/env python
"""advent of code 2023 day 1 part 1"""
lines = open("input.txt").readlines()

numbers = [[n for n in line if n.isnumeric()] for line in lines]

answer = 0
for nums in numbers:
    answer += int(nums[0]+nums[-1])

print("aoc 2023 day 1 part 1:", answer)

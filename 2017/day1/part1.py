#!python
# cython: language_level=3
"""advent of code 2017 day 1 part 1"""

nums = [[int(_) for _ in list(line)] for line in open("input.txt").read().splitlines()][0]

answer = 0
for i, n in enumerate(nums):
    if n == nums[i-1]:
        answer += n

print("part 1: {}".format(answer))

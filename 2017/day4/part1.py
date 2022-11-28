#!python
# cython: language_level=3
"""advent of code 2017 day 4 part 1"""

lines = [[_ for _ in list(line.split())] for line in open("input.txt").read().splitlines()]

answer = 0
for line in lines:
    if len(line) == len(set(line)):
        answer += 1

print("part 1: {}".format(answer))

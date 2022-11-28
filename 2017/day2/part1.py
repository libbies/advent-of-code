#!python
# cython: language_level=3
"""advent of code 2017 day 2 part 1"""

lines = [[int(_) for _ in list(line.split())] for line in open("input.txt").read().splitlines()]

answer = 0
for line in lines:
    answer += max(line) - min(line)

print("part 1: {}".format(answer))

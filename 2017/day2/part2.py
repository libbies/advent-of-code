#!python
# cython: language_level=3
"""advent of code 2017 day 2 part 2"""

lines = [sorted([int(_) for _ in list(line.split())]) for line in open("input.txt").read().splitlines()]

answer = 0
for line in lines:
    answer += [m//n for m in line for n in line if m!=n and m%n==0][0]

print("part 2: {}".format(answer))

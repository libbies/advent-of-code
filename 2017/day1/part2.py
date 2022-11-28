#!python
# cython: language_level=3
"""advent of code 2017 day 1 part 2"""

nums = [[int(_) for _ in list(line)] for line in open("input.txt").read().splitlines()][0]

l = len(nums)
answer = 0
for i, n in enumerate(nums):
    if n == nums[(l//2+i)%l]:
        answer += n

print("part 2: {}".format(answer))

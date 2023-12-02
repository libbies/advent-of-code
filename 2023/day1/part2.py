#!/usr/bin/env python
"""advent of code 2023 day 1 part 2"""
lines = open("input.txt").readlines()

for n, line in enumerate(lines):
    tmp = list(line)
    while True:
        line = ''.join(tmp)
        match = [
            (line.index(s), n)
            for n, s in enumerate([
                "zero", "one", "two", "three", "four",
                "five", "six", "seven", "eight", "nine"])
            if s in line
        ]
        if not match:
            break
        i, number = min(match)
        tmp[i] = str(number)
    lines[n] = ''.join(tmp)

numbers = [[n for n in line if n.isnumeric()] for line in lines]

answer = 0
for nums in numbers:
    answer += int(nums[0] + nums[-1])

print("aoc 2023 day 1 part 2:", answer)

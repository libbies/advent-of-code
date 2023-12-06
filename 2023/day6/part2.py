#!/usr/bin/env python
"""advent of code 2023 day 6 part 2"""
lines = open("input.txt").readlines()

time = int(''.join(c for c in lines[0] if c.isnumeric()))
distance = int(''.join(c for c in lines[-1] if c.isnumeric()))

first = next(n for n in range(time) if n*(time-n)>distance)
last = next(n for n in reversed(range(time)) if n*(time-n)>distance)

answer = last - first + 1
print("aoc 2023 day 6 part 2:", answer)

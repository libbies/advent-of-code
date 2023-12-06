#!/usr/bin/env python
"""advent of code 2023 day 6 part 1"""
lines = open("input.txt").readlines()

times = map(int, lines[0].split()[1:])
distances = map(int, lines[-1].split()[1:])

answer = 1
for time, distance in zip(times, distances):
    answer *= sum(1 for n in range(time) if n*(time-n)>distance)

print("aoc 2023 day 6 part 1:", answer)

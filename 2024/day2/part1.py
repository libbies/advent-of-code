#!/usr/bin/env python3
"""advent of code 2024 day 2 part 1"""

reports = [_.split() for _ in open("input.txt").read().splitlines()]

answer = 0
for report in reports:
    levels = [int(l) for l in report]
    if levels == sorted(levels):
        increasing = True
    elif levels == sorted(levels)[::-1]:
        increasing = False
    else:
        continue
    for i, level in enumerate(levels):
        if i == len(levels)-1:
            answer += 1
        elif levels[i+1] == level:
            break
        elif increasing and levels[i+1]-level > 3:
            break
        elif not increasing and level-levels[i+1] > 3:
            break

print("aoc 2024 day 2 part 1:", answer)

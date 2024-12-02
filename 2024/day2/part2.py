#!/usr/bin/env python3
"""advent of code 2024 day 2 part 2"""

reports = [_.split() for _ in open("input.txt").read().splitlines()]

def check_safety(levels):
    if levels == sorted(levels):
        increasing = True
    elif levels == sorted(levels)[::-1]:
        increasing = False
    else:
        return False
    for i, level in enumerate(levels):
        if i == len(levels)-1:
            return True
        if levels[i+1] == level:
            return False
        if increasing and levels[i+1]-level > 3:
            return False
        if not increasing and level-levels[i+1] > 3:
            return False

answer = 0
for report in reports:
    levels = [int(l) for l in report]
    if check_safety(levels):
        answer += 1
        continue
    tests = [levels[:i] + levels[i+1:] for i in range(len(levels))]
    for test in tests:
        if check_safety(test):
            answer += 1
            break

print("aoc 2024 day 2 part 2:", answer)

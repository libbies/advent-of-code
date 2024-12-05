#!/usr/bin/env python3
"""advent of code 2024 day 5 part 1"""

lines = open("input.txt").read().splitlines()

rules = list()
updates = list()
for line in lines:
    if '|' in line:
        rules += [ [*map(int, line.split('|'))] ]
    if ',' in line:
        updates += [ [*map(int, line.split(','))] ]

answer = 0
for update in updates:
    for rule in rules:
        if rule[0] in update and rule[1] in update:
            if update.index(rule[0]) > update.index(rule[1]):
                break
    else:
        answer += update[len(update)//2]

print("aoc 2024 day 5 part 1:", answer)

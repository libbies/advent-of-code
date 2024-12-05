#!/usr/bin/env python3
"""advent of code 2024 day 5 part 2"""

lines = open("input.txt").read().splitlines()

rules = list()
updates = list()
for line in lines:
    if '|' in line:
        rules += [ [*map(int,line.split('|'))] ]
    if ',' in line:
        updates += [ [*map(int,line.split(','))] ]

incorrect = list()
for update in updates:
    for rule in rules:
        if rule[0] in update and rule[1] in update:
            if update.index(rule[0]) > update.index(rule[1]):
                incorrect.append(update)
                break

answer = 0
for update in incorrect:
    sorted = list()
    applicable = list()
    for rule in rules:
        if rule[0] in update and rule[1] in update:
            applicable += [ rule ]
    while update:
        for page in update:
            for rule in applicable:
                if page==rule[1]:
                    break
            else:
                sorted += [ page ]
                update.remove(page)
                applicable = [ rule for rule in applicable if page!=rule[0] ]
    answer += sorted[len(sorted)//2]

print("aoc 2024 day 5 part 2:", answer)

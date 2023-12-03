#!/usr/bin/env python
"""advent of code 2018 day 5 part 2"""
import string, itertools
polymer = open("input.txt").read().strip()

units = {c: 0 for c in string.ascii_lowercase}
for unit in units:
    tmp = polymer.replace(unit, '').replace(unit.upper(), '')
    reacting = True
    while reacting:
        p = tmp
        for c in string.ascii_lowercase:
            p = p.replace(c + c.upper(), '').replace(c.upper() + c, '')
        if tmp == p:
            reacting = False
        tmp = p
    units[unit] = len(p)

answer = min(units.values())
print("aoc 2018 day 5 part 2:", answer)

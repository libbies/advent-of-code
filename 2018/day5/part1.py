#!/usr/bin/env python
"""advent of code 2018 day 5 part 1"""
import string, itertools
polymer = open("input.txt").read().strip()

reacting = True
while reacting:
    p = polymer
    for c in string.ascii_lowercase:
        p = p.replace(c + c.upper(), '').replace(c.upper() + c, '')
    if polymer == p:
        reacting = False
    polymer = p

answer = len(p)
print("aoc 2018 day 5 part 1:", answer)

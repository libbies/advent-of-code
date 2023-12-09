#!/usr/bin/env python
"""advent of code 2023 day 9 part 1"""
from functools import reduce
lines = (map(int,l.split()) for l in open("input.txt").readlines())

class History(list):
    next, prev = None, None

answer = 0
for line in lines:
    hist = History(line)
    while any(hist):
        hist.next = History(b-a for b,a in zip(hist[1:], hist))
        hist.next.prev = hist
        hist = hist.next
    while hist.prev:
        hist.prev.append(hist.prev[-1] + hist[-1])
        hist = hist.prev
    answer += hist[-1]

print("aoc 2023 day 9 part 1:", answer)

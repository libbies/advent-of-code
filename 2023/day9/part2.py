#!/usr/bin/env python
"""advent of code 2023 day 9 part 2"""
from collections import deque
lines = (map(int,l.split()) for l in open("input.txt").readlines())

class History(deque):
    next, prev = None, None

answer = 0
for line in lines:
    hist = History(line)
    while any(hist):
        hist.next = History(value-hist[i-1] for i, value in enumerate(hist) if i>0)
        hist.next.prev = hist
        hist = hist.next
    while hist.prev:
        hist.prev.appendleft(hist.prev[0] - hist[0])
        hist = hist.prev
    answer += hist[0]

print("aoc 2023 day 9 part 2:", answer)

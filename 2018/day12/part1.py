#!/usr/bin/env python
"""advent of code 2018 day 12 part 1"""
from collections import defaultdict
lines = open("input.txt").read().strip().split('\n', maxsplit=2)

state = defaultdict(lambda: ".", enumerate(lines[0].split()[-1]))

notes = {}
for note, _, output in (_.split() for _ in lines[-1].split('\n')):
    notes[note] = output

def lookup(s, n):
    note = s[n-2] + s[n-1] + s[n] + s[n+1] + s[n+2]
    if note in notes:
        return notes[note]
    return '.'

iterations = 20
while iterations:
    for n in range(1, 2):
        state[min(state)-n] = "."
        state[max(state)+n] = "."
    new = state.copy()
    for n in new.keys():
        new[n]=lookup(state, n)
    state = new
    iterations -= 1

answer = sum(pot for pot,contents in state.items() if contents=="#")
print("aoc 2018 day 12 part 1:", answer)

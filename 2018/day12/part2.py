#!/usr/bin/env python
"""advent of code 2018 day 12 part 2"""
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

iterations = 50000000000
scores = list()
while iterations:
    for n in range(1, 2):
        state[min(state)-n] = "."
        state[max(state)+n] = "."
    new = state.copy()
    scores = scores[-10:] + [sum(pot for pot,contents in state.items() if contents=="#")]
    if len(scores)>=10 and len({score-prev for score,prev in zip(scores[1:], scores)})==1:
        break
    for n in new.keys():
        new[n]=lookup(state, n)
    state = new
    iterations -= 1

answer = (scores[1]-scores[0]) * iterations + sum(p for p,c in state.items() if c=="#")
print("aoc 2018 day 12 part 2:", answer)

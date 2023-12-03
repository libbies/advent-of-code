#!/usr/bin/env python
"""advent of code 2018 day 7 part 1"""
lines = [_.split()[1:8:6] for _ in open("input.txt").read().splitlines()]

steps = {l[0] for l in lines} | {l[1] for l in lines}

paths = {step: list() for step in steps}
for req, end in lines:
    paths[end] += req

answer = ""
while paths:
    step = min(end for end, req in paths.items() if not req)
    answer += step
    paths.pop(step)
    for end, req in paths.items():
        if step in req:
            paths[end].remove(step)

print("aoc 2018 day 7 part 1:", answer)

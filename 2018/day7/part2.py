#!/usr/bin/env python
"""advent of code 2018 day 7 part 2"""
lines = [_.split()[1:8:6] for _ in open("input.txt").read().splitlines()]

steps = {l[0] for l in lines} | {l[1] for l in lines}
workers = {step: 0 for step in steps}
paths = {step: [] for step in steps}
for req, end in lines:
    paths[end] += req

num_workers = 5
duration = 60
answer = -1
while paths:
    answer += 1
    for step, remaining in workers.items():
        if remaining == 1:
            paths.pop(step)
            for end, reqs in paths.items():
                if step in reqs:
                    paths[end].remove(step)
        if remaining > 0:
            workers[step] -= 1
    if num_workers > len([w for w in workers.values() if w]):
        jobs = [
                end for end, reqs in paths.items() if not reqs if not workers[end]
            ][:num_workers-len([w for w in workers.values() if w])]
        for job in jobs:
            workers[job] = duration + ord(job) - 64

print("aoc 2018 day 7 part 2:", answer)

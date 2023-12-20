#!/usr/bin/env python
"""advent of code 2023 day 20 part 2"""
from collections import deque, defaultdict
from math import lcm
lines = [l.split(maxsplit=2) for l in open("input.txt").readlines()]

low, high = 0, 1
class Module(object):
    type = None
    output = low
    inputs = {}
    outputs = []

modules = defaultdict(Module)
for line in lines:
    if line[0][0] in ('%', '&'):
        line[1], line[0] = line[0][0], line[0][1:]
    modules[line[0]] = Module()
    modules[line[0]].type = line[1]
    modules[line[0]].inputs = {}
    modules[line[0]].outputs = line[2].strip().split(', ')

for module in modules:
    for dst in modules[module].outputs:
        if modules.get(dst, Module).type=='&':
            modules[dst].inputs[module] = low

def output(module):
    if modules[module].type=='%':
        return modules[module].output
    elif modules[module].type=='&':
        if all(input==high for input in modules[module].inputs.values()):
            return low
        return high
    return low

targets = dict()
queue = deque()
n = 1
while len(targets)!=4:
    queue.append("broadcaster")
    while queue:
        module = queue.popleft()
        pulse = output(module)
        for dst in modules[module].outputs:
            # hardcoded for my input, (ln, db, vq, tf) -> &tg -> rx
            if dst in ("ln", "db", "vq", "tf"):
                if output(dst)==high and n!=1:
                    targets[dst] = n
            if modules[dst].type=='%' and pulse==low:
                modules[dst].output = not modules[dst].output
                queue.append(dst)
            if modules[dst].type=='&':
                modules[dst].inputs[module] = pulse
                queue.append(dst)
    n += 1

answer = lcm(*(target for target in targets.values()))
print("aoc 2023 day 20 part 2:", answer)

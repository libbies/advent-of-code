#!/usr/bin/env python
"""advent of code 2023 day 20 part 1"""
from collections import deque, defaultdict
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

counts = {high: 0, low: 0}
queue = deque()
for n in range(1000):
    # print("button -low-> broadcaster")
    counts[low] += 1 # pres butan
    queue.append("broadcaster")
    while queue:
        module = queue.popleft()
        pulse = output(module)
        for dst in modules[module].outputs:
            # print(f"{module} -{'high' if pulse else 'low'}-> {dst}")
            if modules[dst].type=='%' and pulse==low:
                modules[dst].output = not modules[dst].output
                queue.append(dst)
            if modules[dst].type=='&':
                modules[dst].inputs[module] = pulse
                queue.append(dst)
            if pulse==high:
                counts[high] += 1
            else:
                counts[low] += 1

answer = counts[low] * counts[high]
print("aoc 2023 day 20 part 1:", answer)

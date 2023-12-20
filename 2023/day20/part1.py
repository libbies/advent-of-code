#!/usr/bin/env python
"""advent of code 2023 day 20 part 1"""
from collections import deque, defaultdict
lines = [l.split(maxsplit=2) for l in open("input.txt").readlines()]

low, high = 0, 1
class Module(object):
    output = low
    inputs = {}

types = defaultdict(str)
outputs = dict()
modules = dict()
for line in lines:
    if line[0][0] in ('%', '&'):
        line[1], line[0] = line[0][0], line[0][1:]
    line[2] = line[2].strip().split(', ')
    types[line[0]] = line[1]
    outputs[line[0]] = deque(line[2])
    modules[line[0]] = Module()
    modules[line[0]].inputs = {}

for module, type in types.items():
    if type=='&':
        for (src, outs) in outputs.items():
            if module in outs:
                # print(f"&{module}", src, outs)
                modules[module].inputs[src] = low

def output(module):
    if types[module]=='%':
        return modules[module].output
    elif types[module]=='&':
        # print(f"{types[module]}{module}", modules[module].inputs)
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
        for dst in outputs[module]:
            # print(f"{module} -{'high' if pulse else 'low'}-> {dst}")
            if types[dst]=='%':
                if pulse==low:
                    modules[dst].output = not modules[dst].output
                    queue.append(dst)
            if types[dst]=='&':
                modules[dst].inputs[module] = pulse
                queue.append(dst)
            if pulse==high:
                counts[high] += 1
            else:
                counts[low] += 1
    # print()

answer = counts[low] * counts[high]
print("aoc 2023 day 20 part 1:", answer)

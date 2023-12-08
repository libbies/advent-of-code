#!/usr/bin/env python
"""advent of code 2023 day 8 part 2"""
import re
from math import lcm

lines = open("input.txt").readlines()

dirs = lines[0].strip()
network = dict()
for line in lines[2:]:
    node, l, r, _ = re.split(r"[^A-Z12]+", line)
    network[node] = (l, r)

step = 0
nodes = [node for node in network if node.endswith('A')]
steps = list()
while nodes:
    nodes = [
        network[node][0] if dirs[step%len(dirs)]=='L' else network[node][-1]
        for node in nodes
    ]
    step += 1
    for node in [n for n in nodes if n.endswith('Z')]:
        nodes.remove(node)
        steps.append(step)

answer = lcm(*steps)
print("aoc 2023 day 8 part 2:", answer)

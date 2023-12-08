#!/usr/bin/env python
"""advent of code 2023 day 8 part 1"""
from re import findall
lines = open("input.txt").readlines()

dirs = lines[0].strip()
network = dict()
for line in lines[2:]:
    node, l, r = findall(r"[A-Z]+", line)
    network[node] = (l, r)

step = 0
node = "AAA"
while node!="ZZZ":
    node = network[node][0] if dirs[step%len(dirs)]=='L' else network[node][-1]
    step += 1

answer = step
print("aoc 2023 day 8 part 1:", answer)

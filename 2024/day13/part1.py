#!/usr/bin/env python3
"""advent of code 2024 day 13 part 1"""
import re

lines = open("input.txt").read().split("\n\n")

answer = 0
for line in lines:
    ax,ay,bx,by,x,y = map(int, re.findall(r"[0-9]+", line))
    for pa in range(x//ax):
        if ax*pa + bx*(pb:=(x-pa*ax)//bx) == x and ay*pa + by*pb == y:
            answer += 3*pa+pb
            break

print("aoc 2024 day 13 part 1:", answer)

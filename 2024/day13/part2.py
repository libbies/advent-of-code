#!/usr/bin/env python3
"""advent of code 2024 day 13 part 2"""
import z3
import re

lines = open("input.txt").read().split("\n\n")

pa, pb = z3.Ints("pa pb")
answer = 0
for line in lines:
    ax,ay,bx,by,x,y = map(int, re.findall(r"[0-9]+", line))
    x += 10_000_000_000_000
    y += 10_000_000_000_000
    solver = z3.Optimize()
    solver.add(pa*ax + pb*bx == x)
    solver.add(pa*ay + pb*by == y)
    solver.add(pa>=0)
    solver.add(pb>=0)
    solver.minimize(3*pa+pb)
    if solver.check() == z3.sat:
        model = solver.model()
        answer += model.eval(3*pa+pb).as_long()

print("aoc 2024 day 13 part 2:", answer)

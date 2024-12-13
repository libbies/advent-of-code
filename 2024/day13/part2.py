#!/usr/bin/env python3
"""advent of code 2024 day 13 part 2"""
import z3

pa, pb = z3.Ints("pa pb")
answer = 0
for _,_,ax,ay,_,_,bx,by,_,x,y in (_.split() for _ in open("input.txt").read().split("\n\n")):
    solver = z3.Optimize()
    ax, ay, bx, by = int(ax[1:-1]), int(ay[1:]), int(bx[1:-1]), int(by[1:])
    x, y = 10_000_000_000_000+int(x[2:-1]), 10_000_000_000_000+int(y[2:])
    solver.add(pa*ax + pb*bx == x)
    solver.add(pa*ay + pb*by == y)
    solver.add(pa>=0)
    solver.add(pb>=0)
    solver.minimize(3*pa+pb)
    if solver.check() == z3.sat:
        model = solver.model()
        answer += model.eval(3*pa+pb).as_long()

print("aoc 2024 day 13 part 2:", answer)

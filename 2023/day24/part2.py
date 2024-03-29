#!/usr/bin/env python
"""advent of code 2023 day 24 part 2"""
import re
import z3
hail = [[int(_) for _ in re.split(r"[^0-9-]+", l.strip())] for l in open("input.txt").readlines()]

Px, Py, Pz = z3.Reals("Px Py Pz")
Vx, Vy, Vz = z3.Reals("Vx Vy Vz")

solver = z3.Solver()
for i, (px, py, pz, vx, vy, vz) in enumerate(hail[:3]):
    t_i = z3.Real(f"t_{i}")
    solver.add(Px + Vx * t_i == px + vx * t_i)
    solver.add(Py + Vy * t_i == py + vy * t_i)
    solver.add(Pz + Vz * t_i == pz + vz * t_i)

assert solver.check() == z3.sat
model = solver.model()
answer = model.eval(Px).as_long() + model.eval(Py).as_long() + model.eval(Pz).as_long()
print("aoc 2023 day 24 part 2:", answer)

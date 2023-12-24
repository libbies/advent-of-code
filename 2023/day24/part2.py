#!/usr/bin/env python
"""advent of code 2023 day 24 part 2"""
import re
from z3 import Int, Ints, Solver, sat
hail = [[int(_) for _ in re.split(r"[^0-9-]+", l.strip())] for l in open("input.txt").readlines()]

Px, Py, Pz = Ints('Px Py Pz')
Vx, Vy, Vz = Ints('Vx Vy Vz')

solver = Solver()
for i, (px, py, pz, vx, vy, vz) in enumerate(hail[:3]):
    t_i = Int(f"t_{i}")
    solver.add(Px + t_i * Vx == px + t_i * vx)
    solver.add(Py + t_i * Vy == py + t_i * vy)
    solver.add(Pz + t_i * Vz == pz + t_i * vz)

assert solver.check() == sat
model = solver.model()
answer = model.eval(Px).as_long() + model.eval(Py).as_long() + model.eval(Pz).as_long()
print("aoc 2023 day 24 part 2:", answer)

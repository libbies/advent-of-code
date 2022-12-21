#!python
"""advent of code 2022 day 21 part 2"""
import z3
lines = [line.split() for line in open("input.txt").read().splitlines()]

solver = z3.Solver()
for line in lines:
    line[0] = line[0][:-1]
    for s in line:
        if type(s)==str and len(s)==4 and not s.isnumeric():
            vars()[s] = z3.Real(s)
    if line[0] == "humn":
        continue
    elif line[0] == "root":
        solver.add(eval(f"{line[1]}=={line[-1]}"))
    else:
        solver.add(eval(f"{line[0]}==" + ''.join(line[1:])))

assert solver.check()==z3.sat
answer = solver.model().eval(humn)

print("part 2:", answer)

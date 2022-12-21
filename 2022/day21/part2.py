#!python
"""advent of code 2022 day 21 part 2"""
import z3
lines = [line.split() for line in open("input.txt").read().splitlines()]

solver = z3.Solver()
for line in lines:
    line[0] = line[0][:-1]
    for s in line:
        if type(s)==str and len(s)==4 and not s.isnumeric():
            exec(f"{s} = z3.Real('{s}')")
    if line[0] == "humn":
        continue
    elif line[0] == "root":
        solver.add(eval(''.join([line[1], "==", line[-1]])))
    else:
        solver.add(eval(''.join([line[0], "=="] + line[1:])))

solver.check()
answer = solver.model()[humn]

print("part 2:", answer)

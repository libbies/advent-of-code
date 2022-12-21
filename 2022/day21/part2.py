#!python
"""advent of code 2022 day 21 part 2"""
import z3
lines = [line.split() for line in open("input.txt").read().splitlines()]

for i, line in enumerate(lines.copy()):
    lines[i][0] = line[0][:-1]

for i, line in enumerate(lines.copy()):
    if line[0] == "root":
        lines[i][2] = "=="

monkeys = dict()
for line in lines.copy():
    if len(line)==2 and line[-1].isnumeric():
        if line[0]=="humn" or line[0]=="root":
            continue
        monkeys[line[0]] = int(line[-1])
        lines.remove(line)

finished = False
while not finished:
    for line in lines.copy():
        finished = True
        if line[0]=="humn" or line[0]=="root":
            continue
        if len(line)==4 and line[1] in monkeys and line[3] in monkeys:
            lines.remove(line)
            finished = False
            if line[2] == "+":
                monkeys[line[0]] = monkeys[line[1]] + monkeys[line[3]]
            if line[2] == "-":
                monkeys[line[0]] = monkeys[line[1]] - monkeys[line[3]]
            if line[2] == "*":
                monkeys[line[0]] = monkeys[line[1]] * monkeys[line[3]]
            if line[2] == "/":
                monkeys[line[0]] = monkeys[line[1]] // monkeys[line[3]]

finished = False
while not finished:
    finished = True
    for i, line in enumerate(lines.copy()):
        if line[0]=="humn" or line[0]=="root":
            continue
        if line[1] in monkeys and line[3] in monkeys:
            lines[i][1]=monkeys[line[1]]
            lines[i][3]=monkeys[line[3]]
            monkeys[line[0]] = eval(''.join(map(str,line[1:4])))
            lines.remove(line)
            finished = False
            break
        elif type(line[1]) in (int, float) and type(line[3]) in (int,float):
            monkeys[line[0]] = eval(''.join(map(str,line[1:4])))
            lines.remove(line)
            finished = False
            break
        if line[1] in monkeys:
            lines[i][1]=monkeys[line[1]]
            finished = False
        if line[3] in monkeys:
            lines[i][3]=monkeys[line[3]]
            finished = False

finished = False
while not finished:
    for line in lines.copy():
        finished = True
        if line[0]=="humn" or line[0]=="root":
            continue

finished = False
queue = dict()
while not finished:
    finished = True
    for line in lines.copy():
        if line[0]=="humn":
            continue
        if any(s for s in line if type(s)==str and "humn" in s):
            queue[line[0]] = line[1:]
            lines.remove(line)
    for i, line in enumerate(lines.copy()):
        if line[0]=="humn":
            continue
        if line[1] in queue:
            lines[i][1] = '(' + ''.join(map(str, queue[line[1]])) + ')'
            finished = False
        if line[3] in queue:
            lines[i][3] = '(' + ''.join(map(str, queue[line[3]])) + ')'
            finished = False

queue["root"][-1] = str(monkeys[queue["root"][-1]])
humn = z3.Int("humn")
solver = z3.Solver()
solver.add(eval(''.join(queue["root"])))
solver.check()

answer = solver.model()[humn]

print("part 2:", answer)

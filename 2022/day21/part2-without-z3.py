#!python
"""advent of code 2022 day 21 part 2"""
lines = [line.split() for line in open("input.txt").read().splitlines()]

for i, line in enumerate(lines.copy()):
    lines[i][0] = line[0][:-1]

for i, line in enumerate(lines.copy()):
    if line[0] == "root":
        lines[i][2] = "=="

monkeys = dict()
finished = False
while not finished:
    finished = True
    for line in lines.copy():
        if line[0] == "humn":
            lines.remove(line)
            finished = False
        elif len(line)==2 and line[-1].isnumeric():
            monkeys[line[0]] = int(line[-1])
            lines.remove(line)
            finished = False
        elif len(line)==4 and line[1] in monkeys and line[3] in monkeys:
            if line[2] == "+":
                monkeys[line[0]] = monkeys[line[1]] + monkeys[line[3]]
            if line[2] == "-":
                monkeys[line[0]] = monkeys[line[1]] - monkeys[line[3]]
            if line[2] == "*":
                monkeys[line[0]] = monkeys[line[1]] * monkeys[line[3]]
            if line[2] == "/":
                monkeys[line[0]] = monkeys[line[1]] // monkeys[line[3]]
            lines.remove(line)
            finished = False

for i, (m0, m1, op, m3) in enumerate(lines.copy()):
    if m1 in monkeys:
        lines[i][1]=monkeys[m1]
    elif m3 in monkeys:
        lines[i][3]=monkeys[m3]
    elif m1 in monkeys and m3 in monkeys:
        lines[i][1]=monkeys[m1]
        lines[i][3]=monkeys[m3]
        monkeys[m0] = eval(''.join(map(str,[m1, op, m3])))
        lines.remove(line)
    elif type(m1) in (int, float) and type(m3) in (int,float):
        monkeys[m0] = eval(''.join(map(str,[m1, op, m3])))
        lines.remove(line)

root = [line for line in lines if line[0]=="root"].pop()
equation = [line for line in lines if line[0]==root[1]]
while equation:
    equation = equation.pop()
    number = equation[1] if type(equation[1])!=str else equation[-1]
    variable = equation[1] if type(equation[1])==str else equation[-1]
    if equation[2] == "*":
        root[-1] //= number
        root[1] = variable
    if equation[2] == "+":
        root[-1] -= number
        root[1] = variable
    if equation[2] == "/":
        if type(equation[1])==str:
            root[1], root[-1] = variable, number * root[-1]
        else:
            root[1], root[-1] = variable, number // root[-1]
    if equation[2] == "-":
        if type(equation[1])==str:
            root[1], root[-1] = variable, number + root[-1]
        else:
            root[1], root[-1] = variable, number - root[-1]
    equation = [line for line in lines if line[0]==root[1]]

answer = root[-1]

print("part 2:", answer)

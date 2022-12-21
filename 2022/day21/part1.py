#!python
"""advent of code 2022 day 21 part 1"""
lines = [line.split() for line in open("input.txt").read().splitlines()]

monkeys = {
    "root": None
}

for line in lines.copy():
    if len(line)==2 and line[-1].isnumeric():
        monkeys[line[0][:-1]] = int(line[-1])
        lines.remove(line)

while not monkeys["root"]:
    for line in lines.copy():
        if len(line)==4 and line[1] in monkeys and line[3] in monkeys:
            lines.remove(line)
            if line[2] == "+":
                monkeys[line[0][:-1]] = monkeys[line[1]] + monkeys[line[3]]
            if line[2] == "-":
                monkeys[line[0][:-1]] = monkeys[line[1]] - monkeys[line[3]]
            if line[2] == "*":
                monkeys[line[0][:-1]] = monkeys[line[1]] * monkeys[line[3]]
            if line[2] == "/":
                monkeys[line[0][:-1]] = monkeys[line[1]] // monkeys[line[3]]

answer = monkeys["root"]

print("part 1:", answer)

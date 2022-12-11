#!python
"""advent of code 2022 day 11 part 1"""
data = [
    [l.split() for l in line.split('\n')]
    for line in open("input.txt").read().split("\n\n")
]

class Monkey():
    def __init__(self, lines):
        self.id = int(lines[0][-1][:-1])
        self.items = [int(_[:-1]) if (',' in _) else int(_) for _ in lines[1][2:]]
        self.op = ' '.join(lines[2][3:])
        self.test = int(lines[3][-1])
        self.true = int(lines[4][-1])
        self.false = int(lines[5][-1])
        self.count = 0
    def __str__(self):
        return f"monkeys[{self.id}]: ({self.items}, {self.op}, {self.test}, {self.true}/{self.false})"

monkeys = dict()
for monkey in data:
    monkeys[int(monkey[0][-1][:-1])] = Monkey(monkey)

round = 0
while round < 20:
    for monkey in monkeys.values():
        monkey.items = [eval(monkey.op)//3 for old in monkey.items]
        monkey.count += len(monkey.items)
        for item in list(monkey.items):
            monkey.items.remove(item)
            if item%monkey.test == 0:
                monkeys[monkey.true].items.append(item)
            else:
                monkeys[monkey.false].items.append(item)
    round += 1

answer = sorted(monkey.count for monkey in monkeys.values())[-2:]
answer = answer[0] * answer[1]
print("part 1:", answer)

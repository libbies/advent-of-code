from pprint import pprint
from collections import defaultdict

instructions = [l.split() for l in open("input.txt").read().splitlines()]

bots = defaultdict(lambda: list())
outputs = dict()

while instructions:
    ins = instructions.pop(0)
    if ins[0] == "value":
        bots[ins[-1]].append(int(ins[1]))
    elif ins[0] == "bot" and len(bots[ins[1]]) >= 2:
        if 17 in bots[ins[1]] and 61 in bots[ins[1]]:
            print(bots[ins[1]], "part1:", ins[1])
        if ins[-7] == "output":
            outputs[int(ins[-6])] = min(bots[ins[1]])
        else:
            bots[ins[-6]].append(min(bots[ins[1]]))
        if ins[-2] == "output":
            outputs[int(ins[-1])] = max(bots[ins[1]])
        else:
            bots[ins[-1]].append(max(bots[ins[1]]))
        del bots[ins[1]]
    else:
        instructions.append(ins)

pprint(("outputs:", sorted(outputs.items(), key=lambda x: x[0])), width=33, compact=True)
print("part2:", outputs[0] * outputs[1] * outputs[2])

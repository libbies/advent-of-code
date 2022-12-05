#!python
"""advent of code 2022 day 5 part 2"""
lines = open("input.txt").read().splitlines()
stacks = [_ for _ in lines if "move" not in _][:-1]
moves = [map(int, _.split()[1::2]) for _ in lines if "move" in _]

crates = { c: list() for c in map(int, stacks[-1].split()) }

for stack in stacks[:-1]:
    for col in range(1, max(crates.keys())*4, 4):
        if stack[col] != " ":
            crates[col//4+1] += stack[col]

for count, src, dst in moves:
    crates[dst] = [crates[src].pop(0) for _ in range(count)] + crates[dst]

answer = ''.join(crates[c][0] for c in crates)

print("part 2:", answer)

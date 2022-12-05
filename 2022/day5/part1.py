#!python
"""advent of code 2022 day 5 part 1"""
lines = open("input.txt").read().splitlines()
stacks = [_ for _ in lines if "move" not in _][:-1]
moves = [map(int, _.split()[1::2]) for _ in lines if "move" in _]

crates = { c: list() for c in map(int, stacks[-1].split()) }

for stack in stacks[:-1]:
    for c in range(1, max(crates.keys())*4, 4):
        if stack[c] != " ":
            crates[c//4+1] += stack[c]

for count, src, dst in moves:
    for _ in range(count):
        crates[dst].insert(0, crates[src].pop(0))

answer = ''.join(crates[c][0] for c in crates)

print("part 1:", answer)

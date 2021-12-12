#!python
"""advent of code 2021 day 12 part 2"""
from collections import defaultdict
lines = [_.split('-') for _ in open("input.txt").read().splitlines()]

paths = defaultdict(list)
for c1,c2 in lines:
    if c2!="start" and c2 not in paths[c1]:
        paths[c1].append(c2)
    if c1!="start" and c1 not in paths[c2]:
        paths[c2].append(c1)

complete = set()
deadends = set()
path = ["start"]
counts = defaultdict(int)
while path:
    for c in paths[path[-1]]:
        if c=="end":
            if tuple(path) not in complete:
                complete.add(tuple(path))
            continue
        if c.islower() and c in path and 2 in counts.values():
            continue
        if tuple(path+[c]) in deadends:
            continue
        if c.islower():
            counts[c] += 1
        path.append(c)
        break
    else:
        deadends.add(tuple(path))
        c = path.pop()
        if c=="start":
            break
        if c.islower():
            counts[c] -= 1

answer = len(complete)
print("aoc 2021 day 12 part 2:", answer)

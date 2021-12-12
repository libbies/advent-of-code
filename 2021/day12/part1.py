"""advent of code 2021 day 12 part 1"""
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
while path:
    for c in paths[path[-1]]:
        if c=="end":
            if tuple(path) not in complete:
                complete.add(tuple(path))
            continue
        if c.islower() and c in path:
            continue
        if tuple(path+[c]) in deadends:
            continue
        path.append(c)
        break
    else:
        deadends.add(tuple(path))
        if path.pop()=="start":
            break

answer = len(complete)
print("aoc 2021 day 12 part 1:", answer)

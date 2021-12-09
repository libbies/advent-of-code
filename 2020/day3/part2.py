#!/usr/bin/env python3
from functools import reduce
from operator import mul

lines = [l.strip() for l in open("input.txt").readlines()]


results = list()
for (right, down) in [(1, 1),(3, 1),(5, 1),(6,1),(1,2)]:
    trees = 0
    for x in range(down, len(lines), down):
        if lines[x][x*right//down%len(lines[x])]=="#":
            trees += 1
    results.append(trees)

print(f"{results} = {reduce(mul, results)}")
# print(eval('*'.join(map(str, results))))

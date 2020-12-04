#!/usr/bin/env python3
from functools import reduce
from operator import mul

lines = [l.strip() for l in open("input.txt").readlines()]


results = [sum([1 for (right, down) in slope for x in range(down, len(lines), down) if lines[x][x*right//down%len(lines[x])]=="#"]) for slope in [(1, 1),(3, 1),(5, 1),(6,1),(1,2)]]

print(f"{results} = {reduce(mul, results)}")

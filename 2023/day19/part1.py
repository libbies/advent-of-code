#!/usr/bin/env python
"""advent of code 2023 day 19 part 1"""
lines = open("input.txt").read().split("\n\n")

flows = dict()
for line in lines[0].splitlines():
    name, flow = line.split('{')
    flows[name] = list()
    for f in flow.strip('}').split(','):
        if ':' in f:
            f = f.split(':')
        flows[name].append(f)

x, m, a, s = [c for c in "xmas"]

parts = list()
for line in lines[-1].splitlines():
    parts.append(eval(line.replace('=', ':')))

answer = 0
for part in parts:
    flow = "in"
    tmp = 0
    while flow and not tmp:
        for f in flows[flow]:
            if isinstance(f, list):
                test, result = f
                test = test.replace('a', "part[a]")
                test = test.replace('x', "part[x]")
                test = test.replace('m', "part[m]")
                test = test.replace('s', "part[s]")
                if eval(test):
                    f = result
                else:
                    continue
            if f in flows:
                flow = f
                break
            if f=="A":
                tmp += sum(part.values())
                break
            if f=="R":
                flow = None
                break
            flow = f
    answer += tmp

print("aoc 2023 day 19 part 1:", answer)

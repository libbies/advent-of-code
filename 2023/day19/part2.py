#!/usr/bin/env python
"""advent of code 2023 day 19 part 2"""
from math import prod
lines = open("input.txt").read().split("\n\n")

flows = dict()
for line in lines[0].splitlines():
    name, flow = line.split('{')
    flows[name] = list()
    for flow in flow.strip('}').split(','):
        if ':' in flow:
            flows[name].append((
                flow[0], flow[1], int(flow[2:].split(':')[0]),
                flow[2:].split(':')[-1]
            ))
        else:
            flows[name].append((None, None, None, flow))

def recurse(ranges, flow, cursor=0):
    if flow=='R':
        return 0
    if flow=='A':
        return prod(end-start+1 for start,end in ranges.values())
    rating, op, n, dst = flows[flow][cursor]
    if not rating:
        return recurse(ranges, dst)
    start, end = ranges[rating]
    if op=='<':
        return (recurse({k:v if k!=rating else (start,n-1) for k,v in ranges.items()}, dst)
              + recurse({k:v if k!=rating else (n,end) for k,v in ranges.items()}, flow, cursor+1)
        )
    if op=='>':
        return (recurse({k:v if k!=rating else (n+1,end) for k,v in ranges.items()}, dst)
              + recurse({k:v if k!=rating else (start,n) for k,v in ranges.items()}, flow, cursor+1)
        )

answer = recurse({k: (1, 4000) for k in "xmas"}, "in")
print("aoc 2023 day 19 part 2:", answer)

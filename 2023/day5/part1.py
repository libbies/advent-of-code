#!/usr/bin/env python
"""advent of code 2023 day 5 part 1"""
lines = open("input.txt").read().split("\n\n")

seeds = [int(n) for n in lines[0].split()[1:]]
maps = dict()
for line in lines[1:]:
    line = line.splitlines()
    src, _, dst = line[0].split()[0].split('-')
    maps[src,dst] = list()
    for dstaddr, srcaddr, incr in [map(int, l.split()) for l in line[1:]]:
        maps[src,dst].append((range(srcaddr, srcaddr+incr), dstaddr-srcaddr))

answer = float('inf')
for seed in seeds:
    src, dst = "seed", None
    while src!="location":
        dst, ranges = [(k[-1],v) for k,v in maps.items() if k[0]==src][0]
        for mapping, delta in ranges:
            if seed in mapping:
                seed = seed + delta
                break
        src, dst = dst, None
    if seed < answer:
        answer = seed

print("aoc 2023 day 5 part 1:", answer)

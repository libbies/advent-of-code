#!/usr/bin/env python
"""advent of code 2023 day 5 part 1"""
lines = open("input.txt").read().split("\n\n")

seeds = [int(n) for n in lines[0].split()[1:]]
maps = dict()
for line in lines[1:]:
    line = line.splitlines()
    src, _, dst = line[0].split()[0].split('-')
    maps[src,dst] = list()
    for dstaddr, srcaddr, length in [map(int, l.split()) for l in line[1:]]:
        maps[src,dst].append((range(srcaddr, srcaddr+length), dstaddr-srcaddr))

answer = max(seeds)
for seed in seeds:
    for m in maps:
        for mapping, delta in maps[m]:
            if seed in mapping:
                seed += delta
                break
    if seed < answer:
        answer = seed

print("aoc 2023 day 5 part 1:", answer)

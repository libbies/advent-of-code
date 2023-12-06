#!/usr/bin/env python
"""advent of code 2023 day 5 part 2"""
lines = open("input.txt").read().split("\n\n")

seeds = [*map(int, lines[0].split()[1:])]
seeds = {"seed": [range(s,s+len) for s,len in zip(seeds[::2], seeds[1::2])]}
maps = dict()
for line in lines[1:]:
    line = line.splitlines()
    src, _, dst = line[0].split()[0].split('-')
    maps[src,dst] = []
    for dstaddr, srcaddr, length in [map(int, l.split()) for l in line[1:]]:
        maps[src,dst].append((range(srcaddr, srcaddr+length), dstaddr-srcaddr))

# i track ranges of numbers instead of the seeds themselves, which are numerous
# and split them up into new ranges as needed
for src, dst in maps:
    seeds[dst] = []
    queue = seeds[src]
    while queue:
        s = queue.pop()
        for d, delta in maps[src,dst]:
            if s.start in d and s.stop-1 in d:
                seeds[dst].append(range(s.start+delta, s.stop+delta))
                break
            if s.start in d and s.stop-1 not in d:
                seeds[dst].append(range(s.start+delta, d.stop+delta))
                queue.append(range(d.stop, s.stop))
                break
            if s.start not in d and s.stop-1 in d:
                queue.append(range(s.start, d.start))
                seeds[dst].append(range(d.start+delta, s.stop+delta))
                break
            if d.start in s and d.stop-1 in s:
                queue.append(range(s.start, d.start))
                seeds[dst].append(range(d.start+delta, d.stop+delta))
                queue.append(range(d.stop, s.stop))
                break
        else:
            seeds[dst].append(s)

answer = min(s.start for s in seeds["location"])
print("aoc 2023 day 5 part 2:", answer)

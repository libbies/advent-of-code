#!python
"""advent of code 2021 day 14 part 1"""
from collections import Counter, defaultdict
lines = open("input.txt").read().splitlines()
polymer = defaultdict(int, Counter(zip(lines[0], lines[0][1:])))
rules = dict()
for line in (l for l in lines if "->" in l):
    pair, _, elem = line.split()
    rules[(pair[0], pair[1])] = elem

step = 0
while step<10:
    step += 1
    merge = defaultdict(int)
    for p in polymer:
        merge[(p[0],rules[p])] += polymer[p]
        merge[(rules[p],p[1])] += polymer[p]
        merge[p] -= polymer[p]
    for p in merge:
        polymer[p] += merge[p]

counts = defaultdict(int)
for p in polymer:
    counts[p[0]] += polymer[p]

elems = sorted(counts.values())
answer = elems[-1] - elems[0] + 1
print("aoc 2021 day 14 part 1:", answer)

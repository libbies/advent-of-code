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
    for p, val in list(polymer.items()):
        polymer[(p[0],rules[p])] += val
        polymer[(rules[p],p[1])] += val
        polymer[p] -= val

counts = defaultdict(int, {lines[0][-1]: 1})
for p, val in polymer.items():
    counts[p[0]] += val

elems = sorted(counts.values())
answer = elems[-1] - elems[0]
print("aoc 2021 day 14 part 1:", answer)

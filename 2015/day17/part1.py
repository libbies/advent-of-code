from functools import lru_cache
from itertools import combinations

containers = sorted(int(i) for i in open("input.txt").read().splitlines())

total = 0
minimum = len(containers)
for n in range(len(containers)):
    for c in combinations(containers, n):
        if sum(c) == 150:
            total += 1

print("part1:", total)

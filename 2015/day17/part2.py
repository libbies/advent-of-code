from functools import lru_cache
from itertools import combinations

containers = sorted(int(i) for i in open("input.txt").read().splitlines())

minimum = len(containers)
for n in range(len(containers)):
    for c in combinations(containers, n):
        if sum(c) == 150:
            if len(c) < minimum:
                minimum = len(c)

print("minimum:", minimum)

total = sum(1 for c in combinations(containers, minimum) if sum(c) == 150)

print("part2:", total)

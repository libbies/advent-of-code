from itertools import combinations
from functools import reduce
from operator import mul

input = [int(l) for l in open("input.txt").read().splitlines()]
set_input = set(input)
l = len(input)
weight = sum(input) // 4

min_packages, max_packages = 0, 0
for n in range(l):
    min_packages = n
    if sum(input[l-n:]) > weight:
        break
for n in range(l):
    if sum(input[:n]) > weight:
        break
    max_packages = n

minimum = reduce(mul, input)
for n in range(min_packages, max_packages):
    for group in combinations(input, n):
        if sum(group) != weight:
            continue
        subset = set_input - set(group)
        found = list()
        for sub_n in range(len(subset)):
            for subgroup in combinations(subset, sub_n):
                if sum(subgroup) == weight:
                    found.append(subgroup)
                    next_subset = subset - set(subgroup)
                    for next_n in range(len(next_subset)):
                        for next_subgroup in combinations(next_subset, next_n):
                            if sum(next_subgroup) == weight:
                                found.append(next_subgroup)
                                break
                        if len(found) == 2:
                            break
                    if len(found) == 2:
                        break
            if len(found) == 2:
                break
        if len(found) != 2:
            continue
        qe = reduce(mul, group)
        if qe < minimum:
            print(group, found, sum(group), qe)
            minimum = qe
    if minimum != reduce(mul, input):
        print("part2:", minimum)
        break

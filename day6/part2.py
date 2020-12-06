from functools import reduce
# from operator import or_

groups = map(str.split, open("input.txt").read().split('\n\n'))

total = 0
for group in groups:
    # total += len(reduce(and_, [set(s) for s in group]))
    total += len(reduce(set.intersection, (set(g) for g in group)))

print(total)

# as one-liner
# print("part2:", sum([len(__import__("functools").reduce(set.intersection, (set(g) for g in group))) for group in map(str.split, open("input.txt").read().split('\n\n'))]))

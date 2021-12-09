# from functools import reduce
# from operator import or_

groups = map(str.split, open("input.txt").read().split('\n\n'))

total = 0
for group in groups:
    # total += len(reduce(or_, [set(s) for s in group]))
    total += len(set.intersection(*[set(g) for g in group]))

print(total)

# as a one-liner
# print("part2:", sum([len(set.intersection(*[set(g) for g in group])) for group in map(str.split, open("input.txt").read().split('\n\n'))]))

from functools import reduce
from operator import or_

groups = map(str.split, open("input.txt").read().split('\n\n'))

total = 0
for group in groups:
    total += len(reduce(or_, [set(s) for s in group]))

print(total)

# as a one-liner
# print(sum([len(__import__("functools").reduce(__import__("operator").or_, [set(s) for s in group])) for group in map(str.split,open("input.txt").read().split('\n\n'))]))

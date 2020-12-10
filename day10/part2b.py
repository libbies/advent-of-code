from functools import reduce
from operator import mul
inputs = sorted(map(int, open("input.txt").read().splitlines()))
counts = ''.join([str(max(1, c-inputs[i-1])) for i, c in enumerate(inputs)]).split('3')
# print("part1:", (len(counts)+1) * (len(''.join(counts))-2))
permutations = [max(1, 2**(len(c)-1)) if len(c)<4 else (2**(len(c)-1))-1 for c in counts]
print("part2:", reduce(mul, permutations))

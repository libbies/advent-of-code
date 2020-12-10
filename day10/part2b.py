from functools import reduce
from operator import mul
inputs = [0] + sorted(map(int, open("input.txt").read().splitlines()))
counts = ''.join([str(c-inputs[i-1]) for i, c in enumerate(inputs)][1:]).split('3')
print("part2:", reduce(mul, [max(1, 2**(len(c)+1-2)) if len(c)+1 <= 4 else ((2**(len(c)+1-2))-1) for c in counts]))

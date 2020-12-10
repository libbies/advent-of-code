from functools import reduce
from itertools import combinations
from operator import mul

inputs = sorted(map(int, open("input.txt").read().splitlines()))
inputs = [0] + inputs + [inputs[-1]+3]

def count_paths(head, tail):
    paths = 0
    if tail - head <= 4:
        paths += 1
    for n in range(1, tail-head-1):
        paths += len([*combinations(inputs[head+1:tail-1], n)])
    return paths

total = 1
head, tail = 0, 0
while tail < len(inputs)-1:
    if (inputs[tail+1] - inputs[tail]) == 3:
        total *= count_paths(head, tail+1)
        head = tail + 1
    tail += 1

print("part2:", total)

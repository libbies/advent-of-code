from functools import reduce
from itertools import combinations
from operator import mul

inputs = sorted(map(int, open("input.txt").read().splitlines()))
inputs = [0] + inputs + [inputs[-1]+3]

def count_paths(head, tail):
    paths = 0
    if tail - head <= 4:
        paths += max(1, 2**(tail-head-2))
    else:
        paths = (2**(tail-head-2)-1)
    return paths
    #paths = 0
    #if tail - head <= 4:
    #    paths += 1
    #for n in range(1, tail-head-1):
    #    paths += len([*combinations(inputs[head+1:tail-1], n)])
    #return paths

total = list()
head, tail = 0, 0
while tail < len(inputs)-1:
    if (inputs[tail+1] - inputs[tail]) == 3:
        count = count_paths(head, tail+1)
        total.append(count)
        print(len(inputs[head:tail+1]), inputs[head:tail+1], count)
        head = tail + 1
    tail += 1

print(total, "part2:", reduce(mul, total))

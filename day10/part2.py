from functools import cache, reduce
from itertools import combinations
from operator import mul

input = sorted(map(int, open("input.txt").read().splitlines()))

inputs = [0] + input + [input[-1]+3]

del input

def count_paths(head, tail):
    if tail - head <= 4:
        paths = 1
    else:
        paths = 0
    for n in range(1, tail-head-1):
        paths += len([*combinations(inputs[head+1:tail-1], n)])
        # print(inputs[head:tail], inputs[head+1:tail-1], n, [*combinations(inputs[head+1:tail-1], n), paths])
    # print("x:", inputs[head:tail], inputs[head+1:tail-1], max(1, paths))
    return max(1, paths)

total = list()
head, tail = 0, 0
while tail < len(inputs)-1:
    if inputs[tail+1] - inputs[tail]==3:
        count = count_paths(head, tail+1)
        total.append(count)
        # print("c:", inputs[head:tail+1], count)
        head = tail + 1
    tail += 1

print(total)
print("part2:", reduce(mul, total))

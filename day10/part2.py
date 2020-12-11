from functools import reduce
from itertools import combinations
from operator import mul, sub

inputs = sorted(map(int, open("input.txt").read().splitlines()))
inputs = [0] + inputs + [inputs[-1]+3]
diffs = [i[1]-i[0] for i in zip(inputs, inputs[1:])]

def count_paths(head, tail):
    paths = 0
    for n in range(len(inputs[head:tail])+1):
        for path in combinations(inputs[head:tail], n):
            if (len(path) <= 1 or inputs[head] not in path
                    or inputs[tail-1] not in path):
                continue
            if max([i[1]-i[0] for i in zip([*path], [*path][1:])]) <= 3:
                paths += 1
    return max(1, paths)

total = 1
head, tail = 0, 0
while tail < len(inputs)-1:
    if (inputs[tail+1] - inputs[tail]) == 3:
        count = count_paths(head, tail+1)
        total *= count
        # print(len(inputs[head:tail+1]), inputs[head:tail+1], count)
        head = tail + 1
    tail += 1

print(f"part2: {total if len(str(total))<=20 else str(total).strip('0')[-10:]} "
      f"len: {len(str(total))}")

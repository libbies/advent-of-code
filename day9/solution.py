from itertools import combinations

input = [*map(int, open("input.txt").read().splitlines())]

sz = 25
key = None
for n in range(len(input)-sz):
    target = input[n+sz]
    for a, b in combinations(input[n:n+sz], 2):
        if a+b == target:
            break
    else:
        print("part1:", target)
        key = target
        break

for x in range(len(input)):
    for y in range(x, len(input)):
        if y-x <= 1:
            continue
        if sum(input[x:y])==key:
            print(x, y, "=> part2:", max(input[x:y])+min(input[x:y]))
            raise(SystemExit)

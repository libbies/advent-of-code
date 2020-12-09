from itertools import combinations

input = [*map(int, open("input.txt").read().splitlines())]

sz = 25
key = None
for n in range(len(input)-sz):
    target = input[n+sz]
    found = False
    for a, b in combinations(input[n:n+sz], 2):
        if a+b == target:
            # print(a,b,a+b,target)
            found = True
            break
    if found:
        continue
    else:
        print(n, found, a, b, "|| part1:", target)
        key = target
        break

for x in range(len(input)-2):
    for y in range(x, len(input)-2):
        if y-x == 1:
            continue
        if sum(input[x:y])==key:
            print(x, y, input[x], input[y], sum(input[x:y]), "|| part2:", max(input[x:y])+min(input[x:y]))
            break

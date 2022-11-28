blocks = sorted([*map(int, l.split('-'))] for l in open("input.txt").read().splitlines())

for block in blocks:
    for b in blocks:
        if b[0] <= block[-1] + 1 <= b[-1]:
            break
    else:
        print("part1:", block[-1] + 1)
        break

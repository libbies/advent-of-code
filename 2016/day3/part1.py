triangles = [
    tuple(int(n) for n in l.strip().split())
    for l in open("input.txt").read().splitlines()
]

valid = 0
for t in triangles:
    if max(t) - min(t) < sum(t) - max(t) - min(t):
        valid += 1

print("part1:", valid)

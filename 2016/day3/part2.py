triangles = [
    tuple(int(n) for n in l.strip().split())
    for l in open("input.txt").read().splitlines()
]

triangles = ([t[0] for t in triangles]
           + [t[1] for t in triangles]
           + [t[2] for t in triangles])

n, valid = 0, 0
while n < len(triangles):
    t = triangles[n:n+3]
    if max(t) - min(t) < sum(t) - max(t) - min(t):
        valid += 1
    n += 3

print("part2:", valid)

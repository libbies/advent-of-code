#!python
"""advent of code 2021 day 22 part 1"""
from collections import defaultdict
lines = open("input.txt").read().splitlines()

cuboids = []
for line in lines:
    value, cuboid = line.split()
    x, y, z = cuboid.split(',')
    x = (int(x.split('=')[-1].split('.')[0]), int(x.split('=')[-1].split('.')[-1]))
    y = (int(y.split('=')[-1].split('.')[0]), int(y.split('=')[-1].split('.')[-1]))
    z = (int(z.split('=')[-1].split('.')[0]), int(z.split('=')[-1].split('.')[-1]))
    cuboids.append((value, (x,y,z)))

grid = defaultdict(lambda:defaultdict(lambda:defaultdict(bool)))
for value, cuboid in cuboids:
    x, y, z = cuboid
    x, y, z = sorted(x), sorted(y), sorted(z)
    flag = 1 if value=="on" else 0
    if max(x)<=-50 or min(x)>=50 or max(y)<=-50 or min(y)>=50 or max(z)<=-50 or min(z)>=50:
        pass
    elif max(x)<=50 and min(x)>=-50 and max(y)<=50 and min(y)>=-50 and max(z)<=50 and min(z)>=-50:
        for cx in range(x[0], x[1]+1):
            for cy in range(y[0], y[1]+1):
                for cz in range(z[0], z[1]+1):
                    grid[cx][cy][cz] = flag

answer = sum(z for x in grid.values() for y in x.values() for z in y.values())
print("aoc 2021 day 22 part 1:", answer)

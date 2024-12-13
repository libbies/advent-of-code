#!/usr/bin/env python3
"""advent of code 2024 day 13 part 1"""

answer = 0
for _,_,ax,ay,_,_,bx,by,_,x,y in (_.split() for _ in open("input.txt").read().split("\n\n")):
    ax,ay = int(ax[1:-1]), int(ay[1:])
    bx,by = int(bx[1:-1]), int(by[1:])
    x,y = int(x[2:-1]), int(y[2:])
    for pa in range(x//ax):
        if ax*pa + bx*(pb:=(x-pa*ax)//bx) == x and ay*pa + by*pb == y:
            cost = 3*pa+pb
            answer += cost
            break

print("aoc 2024 day 13 part 1:", answer)

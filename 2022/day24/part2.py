#!python
"""advent of code 2022 day 24 part 2"""
from copy import deepcopy
grid = [[[c] for c in line] for line in open("input.txt").read().splitlines()]
empty = [[c if c[0]=='#' else [] for c in line] for line in grid]

def pprint(grid=grid):
    for x, line in enumerate(grid):
        print (''.join([c[0] if len(c)==1 else '.' if len(c)==0 else str(len(c)) for c in line]))

max_x = len(grid)
max_y = len(grid[0])
start = (0, grid[0].index(['.']))
end = (max_x-1, grid[-1].index(['.']))

minute = 0
for _ in range(3):
    moves = {start}
    while end not in moves:
        minute += 1
        tmp = deepcopy(empty)
        for x, line in enumerate(grid):
            for y, blizzards in enumerate(line):
                for b in blizzards:
                    if b==">":
                        if y==max_y-2: tmp[x][1].append(">")
                        else:        tmp[x][y+1].append(">")
                    if b=="<":
                        if y==1: tmp[x][max_y-2].append("<")
                        else:        tmp[x][y-1].append("<")
                    if b=="v":
                        if x==max_x-2: tmp[1][y].append("v")
                        else:        tmp[x+1][y].append("v")
                    if b=="^":
                        if x==1: tmp[max_x-2][y].append("^")
                        else:        tmp[x-1][y].append("^")
        grid = tmp
        for (x,y) in moves.copy():
            for m,n in ((-1,0), (1,0), (0,-1), (0,1), (0,0)):
                if (x+m,y+n) in (start,end) or (1<=x+m<=max_x-2 and 1<=y+n<=max_y-2):
                    if grid[x+m][y+n]==[]:
                        moves.add((x+m,y+n))
                    elif (x+m,y+n) in moves:
                        moves.remove((x+m,y+n))
        # pprint(tmp)
        # print(minute, len(moves), max(moves))
    start, end = end, start

answer = minute
print("part 2:", answer)

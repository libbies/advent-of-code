#!python
"""advent of code 2022 day 24 part 1"""
from copy import deepcopy
from collections import defaultdict
grid = [[[c] for c in line] for line in open("input.txt").read().splitlines()]
empty = [[c if c[0]=='#' else [] for c in line] for line in grid]

def pprint(grid=grid):
    for x, line in enumerate(grid):
        print (''.join([c[0] if len(c)==1 else '.' if len(c)==0 else str(len(c)) for c in line]))

max_x = len(grid)
max_y = len(grid[0])
start = (0, grid[0].index(['.']))
end = (max_x-1, grid[-1].index(['.']))

moves = defaultdict(lambda: 0, {start: 1})

round = 0
while end not in moves:
    round += 1
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
    grid = deepcopy(tmp)
    for (x,y), move in moves.copy().items():
        for m,n in [(-1,0), (1,0), (0, -1), (0, 1), (0,0)]:
            if (x+m,y+n) in (start,end) or (1<=x+m<=max_x-2 and 1<=y+n<=max_y-2):
                if grid[x+m][y+n]==[]:
                    moves[x+m,y+n] = round
                else:
                    try:
                        del moves[x+m,y+n]
                    except:
                        pass
    # pprint(tmp)
    # print(round, len(moves), max(moves))

answer = round
print("part 1:", answer)

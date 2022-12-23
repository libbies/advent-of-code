#!python
"""advent of code 2022 day 23 part 2"""
from collections import defaultdict, Counter
lines = [list(line) for line in open("input.txt").read().splitlines()]

grid = defaultdict(lambda: False)
for x, line in enumerate(lines):
    for y, c in enumerate(line):
        if c=='#':
            grid[x,y] = True

def pprint():
    copy = grid.copy()
    min_x = min([k[0] for k in copy])
    max_x = max([k[0] for k in copy])
    min_y = min([k[1] for k in copy])
    max_y = max([k[1] for k in copy])
    for x in range(min_x-1, max_x+2):
        print(x, ''.join(["#" if copy[x,y] else '.' for y in range(min_y-1, max_y+2)]))

# N S W E
dirq = ["x-1,y+i", "x+1,y+i", "x+i,y-1", "x+i,y+1"]
dirs = ["(x-1,y)", "(x+1,y)", "(x,y-1)", "(x,y+1)"]
dir = 0
round = 0
while True:
    round += 1
    tmp = dict()
    copy = grid.copy()
    prev = set(grid.keys())
    for (x,y), value in grid.items():
        if all(not copy[x+i,y+j] for (i,j) in ((-1,-1), (-1,0), (-1,1), (0,-1), (0, 1), (1,-1), (1,0), (1,1))):
            pass
        elif all(not copy[eval(dirq[(dir+0)%4])] for i in (-1, 0, 1)):
            tmp[x,y] = eval(dirs[(dir+0)%4])
        elif all(not copy[eval(dirq[(dir+1)%4])] for i in (-1, 0, 1)):
            tmp[x,y] = eval(dirs[(dir+1)%4])
        elif all(not copy[eval(dirq[(dir+2)%4])] for i in (-1, 0, 1)):
            tmp[x,y] = eval(dirs[(dir+2)%4])
        elif all(not copy[eval(dirq[(dir+3)%4])] for i in (-1, 0, 1)):
            tmp[x,y] = eval(dirs[(dir+3)%4])
    counts = Counter(tmp.values())
    moves = {elf: loc for elf, loc in tmp.items() if counts[loc]==1}
    for elf in moves.keys():
        del grid[elf]
    for loc in moves.values():
        grid[loc] = True
    if len(set(grid.keys()) - prev) == 0:
        answer = round
        break
    dir += 1
    #pprint()

print("part 2:", answer)

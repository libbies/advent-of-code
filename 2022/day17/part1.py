#!python
"""advent of code 2022 day 17 part 1"""
from itertools import cycle

jet = cycle(open("input.txt").read().strip())
grid = []
shapes = ['-', '+', 'L', 'I', 'o']
cursor = 0
limit = 10 # lol

def pprint(lines=100):
    print('\n'.join('║'+''.join(line)+'║' for line in grid[-lines:][::-1])+"\n╚═══════╝")

def move_up():
    for i, line in enumerate(grid):
        if '@' in line and i==0:
            return True
        if '@' not in line or i==0:
            continue
        for j, char in enumerate(line):
            if char=='@' and grid[i-1][j] not in ('.', '@'):
                return True
    for i, line in enumerate(grid):
        if '@' not in line or i<=0:
            continue
        for j, char in enumerate(line):
            if char=='@':
                grid[i-1][j], grid[i][j] = '@', '.'
    return False

def move_left():
    for line in grid:
        if '@' not in line:
            continue
        for j, char in enumerate(line):
            if char=='@' and (j==0
                          or (j!=0 and line[j-1] not in ['.', '@'])):
                return
    for i, line in enumerate(grid):
        if '@' not in line:
            continue
        for j in range(1, 7):
            if grid[i][j]=='@':
                grid[i][j-1], grid[i][j] = '@', '.'

def move_right():
    for line in grid:
        if '@' not in line:
            continue
        for j, char in enumerate(line):
            if char=='@' and (j==6
                          or (j!=6 and line[j+1] not in ['.', '@'])):
                return
    for i, line in enumerate(grid):
        if '@' not in line:
            continue
        for j in range(5,-1,-1):
            if grid[i][j]=='@':
                grid[i][j+1], grid[i][j] = '@', '.'

height = 0
def cleanup():
    global grid, height
    for line in grid:
        if '@' not in line:
            continue
        for j, char in enumerate(line):
            if char=='@':
                line[j] = '#'
    while '#' not in grid[-1]:
        _ = grid.pop()
    if len(grid) > 2*limit:
        # ensure that there's always a '#' block to land on
        if not all('#' in [l[n] for l in grid[-limit:]] for n in range(7)):
            return
        l = len(grid)
        grid = grid[-limit:]
        height += l - limit

while cursor < 2022:
    grid += [['.' for _ in range(7)] for _ in range(4)]
    shape = shapes[cursor%5]
    while shape:
        if shape=='-':
            grid += [list("..@@@@.")]
        elif shape=='+':
            grid += [list("...@...")]
            grid += [list("..@@@..")]
            grid += [list("...@...")]
        elif shape=='L':
            grid += [list("..@@@..")]
            grid += [list("....@..")]
            grid += [list("....@..")]
        elif shape=='I':
            grid += [list("..@....")]
            grid += [list("..@....")]
            grid += [list("..@....")]
            grid += [list("..@....")]
        elif shape=='o':
            grid += [list("..@@...")]
            grid += [list("..@@...")]
        while shape:
            stopped = move_up()
            if stopped:
                shape = None
            elif next(jet)=='>':
                move_right()
            else:
                move_left()
    cursor += 1
    cleanup()

answer = height + len(grid)

print("part 1:", answer)

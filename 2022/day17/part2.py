#!python
"""advent of code 2022 day 17 part 2"""
from itertools import cycle

jets = open("input.txt").read().strip()
len_jets = len(jets)
jets = cycle(jets)
grid = []
shapes = ['-', '+', 'L', 'I', 'o']
limit = 10 # lol

jet_count = 0
def next_jet():
    global jet_count
    jet_count += 1
    return next(jets)

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

heights = {n:[] for n in range(5)}
cursor = 0
while cursor < 1_000_000_000_000:
    # 11 here works for both the example and the puzzle input
    # len(input_jets) % len(example_jets) = 11
    if jet_count%len_jets==11:
        heights[cursor%5].append((cursor, height+len(grid)))
    if jet_count%len_jets==11 and len(heights[cursor%5])%2==1 and len(heights[cursor%5])>=2:
        diffs = [y[-1]-x[-1] for (x,y) in zip(heights[cursor%5], heights[cursor%5][1:])]
        if diffs[:len(diffs)//2]==diffs[len(diffs)//2:]:
            prev_cursor, prev_height = heights[cursor%5][0]
            cycle = cursor - prev_cursor
            height += ((1_000_000_000_000-cursor)//cycle * (height+len(grid)-prev_height))
            cursor = 1_000_000_000_000 - ((1_000_000_000_000-cursor)%cycle)
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
            elif next_jet()=='>':
                move_right()
            else:
                move_left()
    cursor += 1
    cleanup()

answer = height + len(grid)

print("part 2:", answer)

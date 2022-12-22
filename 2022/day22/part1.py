#!python
"""advent of code 2022 day 22 part 1"""
import re, time, code
filename = "input.txt"
grid = [list(line) for line in open(filename).read().splitlines() if "." in line]
max_x = len(grid)
max_y = len(grid[0])
grid = [list(line.ljust(max_y, " ")) for line in open(filename).read().splitlines() if "." in line]

dead = set()
for x in range(max_x):
    for y in range(max_y):
        if grid[x][y]==" ":
            dead.add((x,y))

def pprint():
    print("║" + '\n║'.join([
        ''.join(line) \
        .replace(" #", "║#") \
        .replace("# ", "#║") \
        .replace(" .", "║.") \
        .replace(". ", ".║") \
        .replace("#", "█") + "║" \
    for line in grid]))

steps = [line for line in open(filename).read().splitlines() if "R" in line].pop()
steps = re.findall("([0-9]+)(L|R)", steps) \
    + [(re.findall("[0-9]+$", steps).pop(), "FIN")]

def find_next(point, facing):
    x, y = point
    # print("fn", point, facing, facing%4, (x,y) in dead)
    init = True
    while (x, y) in dead or init:
        init = False
        if facing%4==0:
            y = (y+1)%max_y
        if facing%4==1:
            x = (x+1)%max_x
            # print("fn", (x,y), facing)
        if facing%4==2:
            y = (y-1)%max_y
        if facing%4==3:
            x = (x-1)%max_x
    if grid[x][y]=="#":
        return False
    else:
        return (x,y)

x, y = 0, grid[0].index('.')
dirs = [">", "v", "<", "^"]
facing = 0
for step, turn in steps:
    # print(step, turn)
    for s in range(int(step)):
        if facing%4==0: # >
            if grid[x][(y+1)%max_y] == '#':
                break
            elif (x, (y+1)%max_y) in dead:
                point = find_next((x,y), facing)
                if point:
                    x, y = point
                else:
                    break
            else:
                y = (y+1)%max_y
            grid[x][y] = ">"
        if facing%4==1: # v
            if grid[(x+1)%max_x][y] == '#':
                break
            elif ((x+1)%max_x, y) in dead:
                # print(x, y, facing)
                point = find_next((x,y), facing)
                if point:
                    # print("point", point)
                    x, y = point
                else:
                    break
            else:
                x = (x+1)%max_x
            grid[x][y] = "v"
        if facing%4==2: # <
            if grid[x][(y-1)%max_y] == '#': # here
                break
            elif (x, (y-1)%max_y) in dead:
                point = find_next((x,y), facing)
                if point:
                    x, y = point
                else:
                    break
            else:
                y = (y-1)%max_y
            grid[x][y] = "<"
        if facing%4==3:# ^
            if grid[(x-1)%max_x][y] == '#':
                break
            elif ((x-1)%max_x, y) in dead:
                point = find_next((x,y), facing)
                if point:
                    x, y = point
                else:
                    break
            else:
                x = (x-1)%max_x
            grid[x][y] = "^"
    if turn=="R":
        facing += 1
    elif turn=="L":
        facing -= 1
    else:
        pass
        #pprint()
    if facing%4==0:
        grid[x][y] = ">"
    if facing%4==1:
        grid[x][y] = "v"
    if facing%4==2:
        grid[x][y] = "<"
    if facing%4==3:
        grid[x][y] = "^"


answer = ((x+1)*1000)+((y+1)*4)+(facing%4)

print("part 1:", answer)

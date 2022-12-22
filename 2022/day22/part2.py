#!python
"""advent of code 2022 day 22 part 2"""
import re, time, code, os
filename = "input.txt"
grid = [line for line in open(filename).read().splitlines() if "." in line]
max_x = len(grid)
max_y = len(grid[0])
grid = [list(line.ljust(max_y, " ")) for line in grid]


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
steps = re.findall("([0-9]+)(L|R)", steps) + [(re.findall("[0-9]+$", steps).pop(), "FIN")]

def find_next(point, face):
    x, y = point
    # dirs = [">", "v", "<", "^"]
    if 0<=x<=49 and y==50 and face%4==2: # < OK
        # 0, <, >, x=149-100, y=0
        x, y = (49-x)+100, 0
        face += 2
    elif 0<=x<=49 and y==149 and face%4==0: # > OK
        # 1, >, <, x=149-100, y=99
        x, y = (49-x)+100, 99
        face += 2
    elif 50<=x<=99 and y==50 and face%4==2: # < OK
        # 2, <, v, x=100, y=0-49
        x, y = 100, x-50
        face -= 1
    elif 50<=x<=99 and y==99 and face%4==0: # > OK
        # 2, >, ^, x=49, y=100-149
        x, y = 49, x+50
        face -= 1
    # dirs = [">", "v", "<", "^"]
    elif 100<=x<=149 and y==0 and face%4==2: # < OK
        # 4, <, >, x=0-49, y=50
        x, y = 49-(x-100), 50
        face += 2
    elif 100<=x<=149 and y==99 and face%4==0: # > OK
        # 3, >, <, x=0-49, y=149
        x, y = 49-(x-100), 149
        face += 2
    elif 150<=x<=199 and y==0 and face%4==2: # < OK
        # 5, <, v, x=50-99, y=0
        x, y = 0, x-100
        face -= 1
    elif 150<=x<=199 and y==49 and face%4==0: # >
        # 5, >, ^, x=149, y=50-99
        x, y = 149, x-100
        face -= 1
    # dirs = [">", "v", "<", "^"]
    elif x==0 and 50<=y<=99 and face%4==3: # ^ OK
        # 0, ^, >, x=199-150, y=0
        x, y = y+100, 0
        face += 1
    elif x==0 and 100<=y<=149 and face%4==3: # ^ OK
        # 1, ^, ^, x=199, y=0-49
        x, y = 199, y - 100
        face += 0
    elif x==49 and 100<=y<=149 and face%4==1: # v OK
        # 1, v, <, x = 50-99, y=99
        x, y = y - 50, 99
        face += 1
    elif x==100 and 0<=y<=49 and face%4==3: # ^ OK
        # 4, ^, >, x = 50-99, y=50
        x, y = y + 50, 50
        face += 1
    elif x==149 and 50<=y<=99 and face%4==1: # v OK
        # 3, v, <, x=150-199, y=49
        x, y = y + 100, 49
        face += 1
    elif x==199 and 0<=y<=49 and face%4==1: # v OK
        # 5, v, v, x=0, y=100-149
        x, y = 0, y + 100
        face += 0
    if (x,y) in dead:
        raise StopIteration
    if grid[x][y]=="#":
        return (False, None)
    else:
        return ((x,y), face)

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
                point, face = find_next((x,y), facing)
                if point:
                    x, y = point
                    facing = face
                else:
                    break
            else:
                y = (y+1)%max_y
            grid[x][y] = ">"
        elif facing%4==1: # v
            if grid[(x+1)%max_x][y] == '#':
                break
            elif ((x+1)%max_x, y) in dead:
                point, face = find_next((x,y), facing)
                if point:
                    x, y = point
                    facing = face
                else:
                    break
            else:
                x = (x+1)%max_x
            grid[x][y] = "v"
        elif facing%4==2: # <
            if grid[x][(y-1)%max_y] == '#': # here
                break
            elif (x, (y-1)%max_y) in dead:
                point, face = find_next((x,y), facing)
                if point:
                    x, y = point
                    facing = face
                else:
                    break
            else:
                y = (y-1)%max_y
            grid[x][y] = "<"
        elif facing%4==3:# ^
            if grid[(x-1)%max_x][y] == '#':
                break
            elif ((x-1)%max_x, y) in dead:
                point, face = find_next((x,y), facing)
                if point:
                    x, y = point
                    facing = face
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
        # pprint()



answer = ((x+1)*1000)+((y+1)*4)+(facing%4)

print("part 2:", answer)
# code.interact(local=dict(globals(), **locals()))

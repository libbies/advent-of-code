#!python
"""advent of code 2022 day 14 part 1"""
lines = tuple(line.split(" -> ") for line in open("input.txt").read().splitlines())

min_x = min(int(rock.split(',')[0]) for rocks in lines for rock in rocks)
max_x = max(int(rock.split(',')[0]) for rocks in lines for rock in rocks)
min_y = min(int(rock.split(',')[1]) for rocks in lines for rock in rocks)
max_y = max(int(rock.split(',')[1]) for rocks in lines for rock in rocks)

grid = [[' ' for x in range(max_x+2)] for y in range(max_y+2)]

def pprint():
    print('\n'.join('║'+''.join(_[min_x-1:max_x+1])+'║' for _ in grid[min_y-4:max_y+4]))

for rocks in lines:
    for r1, r2 in zip(rocks, rocks[1:]):
        r1 = tuple(map(int, r1.split(',')))
        r2 = tuple(map(int, r2.split(',')))
        if r1[0]==r2[0]:
            for y in range(min(r1[1],r2[1]), max(r1[1],r2[1])+1):
                grid[y][r1[0]] = '█'
        if r1[1]==r2[1]:
            for x in range(min(r1[0],r2[0]), max(r1[0],r2[0])+1):
                grid[r1[1]][x] = '█'

def drop(x, y):
    if y > max_y:
        return False
    if grid[y+1][x-1]!=' ' and grid[y+1][x]!=' ' and grid[y+1][x+1]!=' ':
        grid[y][x] = 'o'
        return True
    if grid[y+1][x+1]==' ' and grid[y+1][x-1]!=' ' and grid[y+1][x]!=' ':
        return drop(x+1, y+1)
    if grid[y+1][x-1]==' ' and grid[y+1][x]!=' ':
        return drop(x-1, y+1)
    if grid[y+1][x]==' ':
        return drop(x, y+1)

answer = 0
while drop(500, 0):
    answer += 1

pprint()

print("part 1:", answer)

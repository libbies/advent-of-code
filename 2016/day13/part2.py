from pprint import pprint

number = int(open("input.txt").read().strip())

size = 50

grid = dict()
for x in range(-1, size+1):
    for y in range(-1, size+1):
        if x in [-1, size] or y in [-1, size]:
            grid[(x,y)] = '#'
        elif bin(x*x + 3*x + 2*x*y + y + y*y + number).count('1') % 2 == 0:
            grid[(x,y)] = '_'
        else:
            grid[(x,y)] = '#'

grid[(1,1)] = 0

for n in range(size):
    for x in range(size):
        for y in range(size):
            if grid[(x, y)] != '_':
                continue
            neighbors = [
                grid[(x+dx, y)] for dx in (-1, 1) if type(grid[(x+dx, y)])==int
            ] + [
                grid[(x, y+dy)] for dy in (-1, 1) if type(grid[(x, y+dy)])==int
            ]
            if neighbors:
                grid[(x, y)] = min(neighbors) + 1

print("part2:", len([s for s in grid.values() if type(s)==int and s<=50]))

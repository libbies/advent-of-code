input = open("input.txt").read()

grid = dict()
x, y = 0, 0
rx, ry = 0, 0
grid[f"{x},{y}"] = True
grid[f"{rx},{ry}"] = True
santa=True
for c in input:
    if santa==True:
        if c == ">":
            x += 1
        if c == "<":
            x -= 1
        if c == "^":
            y += 1
        if c == "v":
            y -= 1
        grid[f"{x},{y}"] = True
    else:
        if c == ">":
            rx += 1
        if c == "<":
            rx -= 1
        if c == "^":
            ry += 1
        if c == "v":
            ry -= 1
        grid[f"{rx},{ry}"] = True
    santa = not santa

print("part2:", len(grid))

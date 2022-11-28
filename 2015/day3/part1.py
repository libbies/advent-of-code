input = open("input.txt").read()

grid = dict()
x, y = 0, 0
grid[f"{x},{y}"] = True
for c in input:
    if c == ">":
        x += 1
    if c == "<":
        x -= 1
    if c == "^":
        y += 1
    if c == "v":
        y -= 1
    grid[f"{x},{y}"] = True

print("part1:", len(grid))

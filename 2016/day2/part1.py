instructions = open("input.txt").read().splitlines()


grid = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
]

x, y = 1, 1
print("part1: ", end="")
for key in instructions:
    for instruction in key:
        if instruction == "L":
            y = max(0, y - 1)
        elif instruction == "R":
            y = min(2, y + 1)
        elif instruction == "U":
            x = max(0, x - 1)
        elif instruction == "D":
            x = min(2, x + 1)
    print(grid[x][y], end="")

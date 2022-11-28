instructions = open("input.txt").read().splitlines()

_, A, B, C, D = None, "A", "B", "C", "D"
grid = [
    [_,_,_,_,_,_,_],
    [_,_,_,1,_,_,_],
    [_,_,2,3,4,_,_],
    [_,5,6,7,8,9,_],
    [_,_,A,B,C,_,_],
    [_,_,_,D,_,_,_],
    [_,_,_,_,_,_,_],
]

x, y = 3, 1
print("part2: ", end="")
for key in instructions:
    for instruction in key:
        if instruction == "L":
            if grid[x][y-1] is not None:
                y -= 1
        elif instruction == "R":
            if grid[x][y+1] is not None:
                y += 1
        elif instruction == "U":
            if grid[x-1][y] is not None:
                x -= 1
        elif instruction == "D":
            if grid[x+1][y] is not None:
                x += 1
    print(grid[x][y], end="")

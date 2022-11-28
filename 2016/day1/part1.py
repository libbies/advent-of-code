instructions = open("input.txt").read().strip().split(', ')

locations = set()
x, y = 0, 0
direction = 4 * len(instructions)
for instruction in instructions:
    turn = instruction[0]
    distance = int(instruction[1:])
    if turn == "L":
        direction -= 1
    elif turn == "R":
        direction += 1
    if direction % 4 == 0:
        y += distance
    elif direction % 4 == 1:
        x += distance
    elif direction % 4 == 2:
        y -= distance
    elif direction % 4 == 3:
        x -= distance

print(x, y, "part1:", abs(x)+abs(y))

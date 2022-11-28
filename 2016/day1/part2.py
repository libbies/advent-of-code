instructions = open("input.txt").read().strip().split(', ')

x, y = 0, 0
locations = {(x, y)}
def check(lx, ly):
    if (lx, ly) in locations:
        print(lx, ly, "part2:", abs(lx) + abs(ly))
        raise SystemExit
    locations.add((lx, ly))

direction = 4 * len(instructions)
for instruction in instructions:
    turn = instruction[0]
    distance = int(instruction[1:])
    if turn == "L":
        direction -= 1
    elif turn == "R":
        direction += 1
    if direction % 4 == 0:
        for n in range(1, distance+1):
            y += 1
            check(x, y)
    elif direction % 4 == 1:
        for n in range(1, distance+1):
            x += 1
            check(x, y)
    elif direction % 4 == 2:
        for n in range(1, distance+1):
            y -= 1
            check(x, y)
    elif direction % 4 == 3:
        for n in range(1, distance+1):
            x -= 1
            check(x, y)

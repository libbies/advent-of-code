lines = open("input.txt").read().splitlines()

facing = {
    0 : 'N',
    90: 'E',
    180: 'S',
    270: 'W'
}
x, y, z = 0, 0, 90
for line in lines:
    action = line[0]
    value = int(line[1:])
    if action=="N" or (action=="F" and z==0):
        x += value
    if action=="S" or (action=="F" and z==180):
        x -= value
    if action=="E" or (action=="F" and z==90):
        y += value
    if action=="W" or (action=="F" and z==270):
        y -= value
    if action=="L":
        z -= value
        if z < 0:
            z += 360
    if action=="R":
        z += value
        if z >= 360:
            z -= 360
    # print(action, value, x, y, z, facing[z])

print(x, y, z, "part1:", abs(x)+abs(y))

lines = open("input.txt").read().splitlines()

x, y = 0, 0
wx, wy = 1, 10
for line in lines:
    action = line[0]
    value = int(line[1:])
    if action=="N":
        wx += value
    if action=="S":
        wx -= value
    if action=="E":
        wy += value
    if action=="W":
        wy -= value
    while value and action=="L":
        if (wx >= 0 <= wy): # northeast -> northwest
            wx, wy = abs(wy), -1 * abs(wx)
        elif (wx >= 0 >= wy): # northwest -> southwest
            wx, wy = -1 * abs(wy), -1 * abs(wx)
        elif (wx <= 0 >= wy): # southwest -> southeast
            wx, wy = -1 * abs(wy), abs(wx)
        elif (wx <= 0 <= wy): # southeast -> northeast
            wx, wy = abs(wy), abs(wx)
        value -= 90
    while value and action=="R":
        if (wx >= 0 <= wy): # northeast -> southeast
            wx, wy = -1 * abs(wy), abs(wx)
        elif (wx <= 0 <= wy): # southeast -> southwest
            wx, wy = -1 * abs(wy), -1 * abs(wx)
        elif (wx <= 0 >= wy): # southwest -> northwest
            wx, wy = abs(wy), -1 * abs(wx)
        elif (wx >= 0 >= wy): # northwest -> northeast
            wx, wy = abs(wy), abs(wx)
        value -= 90
    if action=="F":
        x += value * wx
        y += value * wy

print('    ', f"x:{x} y:{y} wx:{wx} wy:{wy}, {abs(x)+abs(y)}")

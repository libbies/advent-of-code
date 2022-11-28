discs = {
    int(l[1].strip('#')): (int(l[-1].strip('.')), int(l[3]))
    for l in (l.split() for l in open("input.txt").read().splitlines())
}

discs[7] = (0, 11)

n = 0
while not (0==(discs[1][0] + 1 + n) % discs[1][1]
            ==(discs[2][0] + 2 + n) % discs[2][1]
            ==(discs[3][0] + 3 + n) % discs[3][1]
            ==(discs[4][0] + 4 + n) % discs[4][1]
            ==(discs[5][0] + 5 + n) % discs[5][1]
            ==(discs[6][0] + 6 + n) % discs[6][1]
            ==(discs[7][0] + 7 + n) % discs[7][1]):
    n += 1

print("part2:", n)

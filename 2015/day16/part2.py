lines = open("input.txt").read().splitlines()

parameters = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1,
}

for line in lines:
    l = line.split(': ', maxsplit=1)[-1]
    for l in l.split(', '):
        l = l.split(': ')
        if l[0] in ("cats", "trees") and parameters[l[0]] < int(l[1]):
            continue
        if l[0] in ("pomeranians", "goldfish") and parameters[l[0]] > int(l[1]):
            continue
        if parameters[l[0]] == int(l[1]):
            continue
        break
    else:
        print("part2:", line)
        break

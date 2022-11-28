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
        if parameters[l[0]] != int(l[1]):
            break
    else:
        print("part1:", line)
        break

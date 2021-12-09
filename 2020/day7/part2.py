from functools import cache

lines = open("input.txt").read().splitlines()

bags = dict()
for line in lines:
    bag = line.split(' contain ')[0].rsplit(maxsplit=1)[0]
    contents = line.split(' contain ')[1].split(', ')
    contents = [c.split(maxsplit=1) for c in contents]
    bags[bag] = [(c, b.rsplit(maxsplit=1)[0]) for c, b in contents]

@cache
def search(bag):
    if bag not in bags or bags[bag]==[('no', 'other')]:
        return(1)
    s = 1
    for (c, b) in bags[bag]:
        s += int(c) * search(b)
    return(s)

print("part2:", search("shiny gold")-1)

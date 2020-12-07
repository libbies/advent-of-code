lines = open("input.txt").read().splitlines()

bags = dict()
for line in lines:
    bag = line.split(' contain ')[0]
    contents = line.split(' contain ')[1].split(', ')
    bags[bag] = [b.split(maxsplit=1) for b in contents]

inner = dict()
queue = ["shiny gold"]
while queue:
    for bag, contents in bags.items():
        if bag.startswith(queue[0]):
            inner[bag.rsplit(maxsplit=1)[0]] = [
                    (c[0], c[1].rsplit(maxsplit=1)[0]) for c in contents
                ]
            queue += [c[1].rsplit(maxsplit=1)[0] for c in contents]
    queue.pop(0)

def search(bag):
    if bag not in inner or inner[bag]==[('no', 'other')]:
        return(1)
    s = 0
    for (c, b) in inner[bag]:
        s += int(c) * search(b)
    return(1+s)

print("part2:", search("shiny gold")-1)

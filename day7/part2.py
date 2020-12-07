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
            # print(queue[0], bag, [c[1] for c in contents])
            inner[bag.rsplit(maxsplit=1)[0]] = [(c[0], c[1].rsplit(maxsplit=1)[0]) for c in contents]
            queue += [c[1].rsplit(maxsplit=1)[0] for c in contents if c[0]!="no"]
    # print(queue)
    _ = queue.pop(0)

def search(bag):
    global inner
    if bag in inner:
        if inner[bag]==[('no', 'other')]:
            return(1)
        s = 0
        for (c,b) in inner[bag]:
            # print(bag, c, b)
            s += int(c) * search(b)
        # print(bag, repr(inner[bag]), s)
        return(1+s)

print(search("shiny gold")-1)

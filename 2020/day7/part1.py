lines = open("input.txt").read().splitlines()

bags = dict()
for line in lines:
    bag = line.split(' contain ')[0]
    contents = line.split(' contain ')[1].split(', ')
    bags[bag] = [b.split(maxsplit=1) for b in contents]

outer = dict()
queue = ["shiny gold"]
while queue:
    for bag, contents in bags.items():
        if [c[1] for c in contents if c[1].startswith(queue[0])]:
            outer[bag] = (queue[0], [c[1] for c in contents])
            queue.append(bag.rsplit(maxsplit=1)[0])
    queue.pop(0)

print("part1:", len(outer))

from itertools import permutations

lines = [l.split() for l in open("input.txt").read().splitlines()]

places = set()
dists = dict()
for line in lines:
    place = tuple(sorted((line[0],line[2])))
    places.update(place)
    dists[place] = int(str(line[-1]))

maximum, minimum = 0, sum(dists.values())
for p in permutations(places, len(places)):
    distance = 0
    for n in range(1, len(p)):
        place = tuple(sorted((p[n-1],p[n])))
        distance += dists[place]
    if distance < minimum:
        minimum = distance
        print("min:", p, minimum)
    elif distance > maximum:
        maximum = distance
        print("max:", p, maximum)

print("part1:", minimum)
print("part2:", maximum)

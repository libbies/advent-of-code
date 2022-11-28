from itertools import permutations
from collections import defaultdict

lines = open("input.txt").read().splitlines()

persons = set()
happiness = defaultdict(lambda: 0)
for line in lines:
    l = line.strip('.').split()
    persons.add(l[0])
    if l[2]=="gain":
        happiness[(l[0], l[-1])] = int(l[3])
    else:
        happiness[(l[0], l[-1])] = -1 * int(l[3])

max_happy = 0
for table in permutations(persons, len(persons)):
    total = 0
    for n in range(len(table)):
        total += happiness[(table[n-1], table[n])] + happiness[(table[n], table[n-1])]
    if total > max_happy:
        max_happy = total
        print(max_happy, table)

print("part1:", max_happy)

persons.add("myself")
max_happy = 0
for table in permutations(persons, len(persons)):
    total = 0
    for n in range(len(table)):
        total += happiness[(table[n-1], table[n])] + happiness[(table[n], table[n-1])]
    if total > max_happy:
        max_happy = total
        print(max_happy, table)

print("part2:", max_happy)

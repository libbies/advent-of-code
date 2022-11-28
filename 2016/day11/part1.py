import re
from pprint import pprint
from copy import deepcopy
floors = {
    n+1: l[-1].split(", ") if "nothing" not in l[-1] else list()
    for n, l in enumerate(
        l.split(maxsplit=4) for l in open("input.txt").read().splitlines()
    )
}

for floor in floors:
    if len(floors[floor]) == 1 and "and" in floors[floor][0]:
        floors[floor] = floors[floor][0].split(' and ')

for floor in floors:
    floors[floor] = [
        [f[:2] for f in f.split()][-2:] for f in floors[floor]
    ]

pprint(floors, width=140)

state = deepcopy(floors)

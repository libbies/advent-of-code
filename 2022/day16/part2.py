#!python
"""advent of code 2022 day 16 part 2"""
import re, collections, functools
lines = [line.split("; ") for line in open("input.txt").read().splitlines()]

valves = dict()
tunnels = collections.defaultdict(lambda: 30)
for room, tunnel in lines:
    valves[room.split()[1]] = int(room.split("=")[-1])
    for r in re.findall("[A-Z]+", tunnel):
        tunnels[room.split()[1], r] = 1

finished = False
while not finished:
    finished = True
    for r1 in valves:
        for r2 in valves:
            for r3 in valves:
                distance = tunnels[r1,r3] + tunnels[r3,r2]
                if distance < tunnels[r1,r2]:
                    tunnels[r1,r2] = distance
                    finished = False

@functools.cache
def search(room, unopened, minutes, elephant):
    flow = 0
    for valve in unopened:
        if tunnels[room,valve] < minutes:
            flow = max(flow,
                search("AA", unopened, 26, False) if (elephant and minutes<13) else 0,
                search(valve, tuple(v for v in unopened if v!=valve),
                       minutes-tunnels[room,valve]-1, elephant)
                    + (minutes-tunnels[room,valve]-1) * valves[valve]
            )
    return flow

answer = search("AA", tuple(v for v,flow in valves.items() if flow!=0), 26, True)

print(search.cache_info())
print("part 2:", answer)

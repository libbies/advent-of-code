#!python
"""advent of code 2022 day 19 part 2"""
import re, functools
lines = [re.findall("[0-9]+", line) for line in open("input.txt").read().splitlines()]
lines = lines[:3]

blueprints = dict()
for id, ore, clay, obs1, obs2, geo1, geo2 in lines:
    blueprints[int(id)] = (
        (int(ore),  0,          0,          0),
        (int(clay), 0,          0,          0),
        (int(obs1), int(obs2),  0,          0),
        (int(geo1), 0,          int(geo2),  0),
    )

@functools.cache
def add(a, b):
    i, j, k, l = a
    m, n, o, p = b
    return (i+m, j+n, k+o, l+p)

@functools.cache
def sub(a, b):
    i, j, k, l = a
    m, n, o, p = b
    return (i-m, j-n, k-o, l-p)

@functools.cache
def cost(mats, mat):
    return all(c>=0 for c in sub(mats, mat))

@functools.cache
def limit(robots, costs, index):
    """limit number of robots to max cost for that material"""
    return robots[index] < max(c[index] for c in costs)

@functools.cache
def iterate(minutes, costs, robots, mats):
    if minutes == 0:
        return mats[-1]
    ore, clay, obsidian, geode = costs
    geodes = 0
    if cost(mats, geode):
        geodes = max(geodes, iterate(minutes-1, costs, add(robots,(0,0,0,1)), add(sub(mats,geode),robots)))
    elif limit(robots, costs, 2) and cost(mats, obsidian):
        geodes = max(geodes, iterate(minutes-1, costs, add(robots,(0,0,1,0)), add(sub(mats,obsidian),robots)))
    elif limit(robots, costs, 2) and limit(robots, costs, 1) and cost(mats, clay):
        geodes = max(geodes, iterate(minutes-1, costs, add(robots,(0,1,0,0)), add(sub(mats,clay),robots)))
    else:
        geodes = max(geodes, iterate(minutes-1, costs, robots, add(mats,robots)))
    if limit(robots, costs, 2) and limit(robots, costs, 1) and limit(robots, costs, 0) and cost(mats, ore):
        geodes = max(geodes, iterate(minutes-1, costs, add(robots,(1,0,0,0)), add(sub(mats,ore),robots)))
    return geodes

answer = 1
for id, (ore, clay, obsidian, geode) in blueprints.items():
    quality = iterate(32, (ore, clay, obsidian, geode), (1, 0, 0, 0), (0, 0, 0, 0))
    answer *= quality

print("add:", add.cache_info())
print("sub:", sub.cache_info())
print("cost:", cost.cache_info())
print("limit:", limit.cache_info())
print("iterate:", iterate.cache_info())
print("part 2:", answer)

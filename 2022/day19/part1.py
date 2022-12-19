#!python
"""advent of code 2022 day 19 part 1"""
import re, functools
lines = [re.findall("[0-9]+", line) for line in open("input.txt").read().splitlines()]

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
def cost(mats, robot):
    """check if there are enough mats for the cost of a robot"""
    return all(c>=0 for c in sub(mats, robot))

@functools.cache
def limit(robots, costs, index):
    """limit number of robots to max cost for that material"""
    return robots[index] < max(c[index] for c in costs)

best = 0
@functools.cache
def iterate(minutes, costs, robots, mats):
    global best
    if minutes<=1 or best>=mats[-1] + minutes*robots[-1] + sum(range(minutes)):
        return mats[-1] + minutes*robots[-1]
    geodes = mats[-1] + (minutes-1)*robots[-1]
    if cost(mats, geode):
        return iterate(minutes-1, costs, add(robots,(0,0,0,1)), add(sub(mats,geode),robots))
    if cost(mats, ore) and limit(robots, costs, 0) and limit(robots, costs, 1) \
                       and limit(robots, costs, 2):
        geodes = max(geodes,
                     iterate(minutes-1, costs, add(robots,(1,0,0,0)), add(sub(mats,ore),robots)))
    if cost(mats, clay) and limit(robots, costs, 1) and limit(robots, costs, 2):
        geodes = max(geodes,
                     iterate(minutes-1, costs, add(robots,(0,1,0,0)), add(sub(mats,clay),robots)))
    if cost(mats, obsidian) and limit(robots, costs, 2):
        geodes = max(geodes,
                     iterate(minutes-1, costs, add(robots,(0,0,1,0)), add(sub(mats,obsidian),robots)))
    geodes = max(geodes, iterate(minutes-1, costs, robots, add(mats,robots)))
    best = max(best, geodes)
    return geodes

answer = 0
for id, (ore, clay, obsidian, geode) in blueprints.items():
    best = 0
    answer += id * iterate(24, (ore, clay, obsidian, geode), (1, 0, 0, 0), (0, 0, 0, 0))

print("add:", add.cache_info())
print("sub:", sub.cache_info())
print("cost:", cost.cache_info())
print("limit:", limit.cache_info())
print("iterate:", iterate.cache_info())
print("part 1:", answer)

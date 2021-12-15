#!python
"""advent of code 2021 day 15 part 2"""
from itertools import chain

lines = open("input.txt").read().splitlines()
l = len(lines)
riskmap = {x: {y: 0 for y in range(l*5)} for x in range(l*5)}
for x, line in enumerate(lines):
    for y, r in enumerate(line):
        r = int(r)
        for w in range(5):
            for z in range(5):
                riskmap[x+(w*l)][y+(z*l)] = r+w+z if r+w+z<=9 else r+w+z-9

l = len(riskmap)
scoreboard = {x: {y: 0 for y in range(l)} for x in range(l)}
# the initial base risk of each position is the risk of the position itself
# plus the lesser of the neighbor to the right (y+1) or below (x+1)
scoreboard[l-1][l-1] = riskmap[l-1][l-1]
for n in reversed(range(l-1)):
    scoreboard[n][l-1] = riskmap[n][l-1] + scoreboard[n+1][l-1]
    scoreboard[l-1][n] = riskmap[l-1][n] + scoreboard[l-1][n+1]

for x in reversed(range(l-1)):
    for y in reversed(range(l-1)):
        if scoreboard[x+1][y] < scoreboard[x][y+1]:
            scoreboard[x][y] = riskmap[x][y] + scoreboard[x+1][y]
        else:
            scoreboard[x][y] = riskmap[x][y] + scoreboard[x][y+1]

# we can then further refine each position score by comparing to their neighbors
# and adjusting the score when a neighbor has a lower score than a position.
# we loop until the score for the starting position (0,0) has reached minimum
best = scoreboard[0][0]
while True:
    for x in chain(range(l), reversed(range(l))):
        for y in chain(range(l), reversed(range(l))):
            scoreboard[x][y] = riskmap[x][y] + min(
                scoreboard[x-1][y] if x>0 else best,
                scoreboard[x+1][y] if x<l-1 else best,
                scoreboard[x][y-1] if y>0 else best,
                scoreboard[x][y+1] if y<l-1 else best,
            )
    if best>scoreboard[0][0]:
        best = scoreboard[0][0]
    else:
        break

answer = scoreboard[0][0] - riskmap[0][0]
print("aoc 2021 day 15 part 2:", answer)

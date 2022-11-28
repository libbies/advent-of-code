#!python
"""advent of code 2021 day 23 part 1"""
lines = open("input.txt").read().splitlines()
row0 = list(lines[2][3:-2:2])
row1 = list(lines[3][3:-1:2])

hallway  = [list() for _ in range(11)]
rooms    = [list() for _ in range(11)]
rooms[2] = [row0[0], row1[0]]
rooms[4] = [row0[1], row1[1]]
rooms[6] = [row0[2], row1[2]]
rooms[8] = [row0[3], row1[3]]

print(hallway)
print(rooms)

answer = 0
print("aoc 2021 day 23 part 1:", answer)

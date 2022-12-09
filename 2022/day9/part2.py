#!python
"""advent of code 2022 day 9 part 1"""
lines = [line.split() for line in open("input.txt").read().splitlines()]

locations = set()
rope = [[0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0]]

def pull(head, tail):
    while True:
        if tail[0] > head[0]+1 and tail[1]==head[1]: # tail 2 above head
            tail[0] -= 1
        elif tail[0] < head[0]-1 and tail[1]==head[1]: # tail 2 below head
            tail[0] += 1
        elif tail[1] > head[1]+1 and tail[0]==head[0]: # tail 2 right of head
            tail[1] -= 1
        elif tail[1] < head[1]-1 and tail[0]==head[0]: # tail 2 left of head
            tail[1] += 1
        elif ((tail[0] > head[0]+1 and tail[1] > head[1]) or # tail 2 above and right of head
                (tail[0] > head[0] and tail[1] > head[1]+1)): # tail above and 2 right of head
            tail[0] -= 1
            tail[1] -= 1
        elif ((tail[0] < head[0]-1 and tail[1] < head[1]) or # tail 2 below and left of head
                (tail[0] < head[0] and tail[1] < head[1]-1)): # tail left and 2 below of head
            tail[0] += 1
            tail[1] += 1
        elif ((tail[0] > head[0]+1 and tail[1] < head[1]) or # tail 2 above and left of head
                (tail[0] > head[0] and tail[1] < head[1]-1)): # tail above and 2 left of head
            tail[0] -= 1
            tail[1] += 1
        elif ((tail[0] < head[0]-1 and tail[1] > head[1]) or # tail 2 below and left of head
                (tail[0] < head[0] and tail[1] > head[1]+1)): # tail left and 2 below of head
            tail[0] += 1
            tail[1] -= 1
        else:
            break
    return tail

for direction, steps in lines:
    steps = int(steps)
    locations.add(tuple(rope[-1]))
    while steps > 0:
        if direction in ["U", "D"]:
            rope[0] = [rope[0][0]-1 if direction=="D" else rope[0][0]+1, rope[0][1]]
        elif direction in ["L", "R"]:
            rope[0] = [rope[0][0], rope[0][1]-1 if direction=="L" else rope[0][1]+1]
        steps -= 1
        for n in range(9):
            rope[1+n] = pull(rope[0+n], rope[1+n])
        locations.add(tuple(rope[-1]))

answer = len(locations)

print("part 2:", answer)

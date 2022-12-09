#!python
"""advent of code 2022 day 9 part 1"""
lines = [line.split() for line in open("input.txt").read().splitlines()]

locations = set()
head = [0,0]
tail = [0,0]

for direction, steps in lines:
    steps = int(steps)
    locations.add(tuple(tail))
    while steps > 0:
        if direction in ["U", "D"]:
            head = [head[0]-1 if direction=="D" else head[0]+1, head[1]]
        elif direction in ["L", "R"]:
            head = [head[0], head[1]-1 if direction=="L" else head[1]+1]
        steps -= 1
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
            locations.add(tuple(tail))

answer = len(locations)

print("part 1:", answer)

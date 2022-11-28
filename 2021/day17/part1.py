#!python
"""advent of code 2021 day 17 part 1"""
import re

start_x, end_x, bottom_y, top_y = (
    int(n) for n in re.findall("[-0-9]+", open("input.txt").read())
)

search_size = 1000 # brute force, it works for the puzzle input, okay :(

answer = (0, None)
for x in range(search_size):
    for y in range(-search_size, search_size):
        pos_x, pos_y, max_y = 0, 0, 0
        vel_x, vel_y = x, y
        while True:
            pos_x += vel_x
            pos_y += vel_y
            if pos_y > max_y:
                max_y = pos_y
            if start_x<=pos_x<=end_x and bottom_y<=pos_y<=top_y and max_y>answer[0]:
                answer = (max_y, (x,y))
            vel_x -= (vel_x>0) - (vel_x<0)
            vel_y -= 1
            if vel_x==0 and not(start_x<=pos_x<=end_x):
                # zero x velocity and not in the target area
                break
            if vel_y <= 0 and bottom_y >= pos_y:
                # negative y velocity and past the bottom of the target area
                break
            if pos_x >= end_x:
                # past the right side the of the target area
                break

print("aoc 2021 day 17 part 1:", answer)

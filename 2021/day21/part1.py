#!python
"""advent of code 2021 day 21 part 1"""
position = dict()
position[1], position[2] = [int(l.split()[-1]) for l in open("input.txt").read().splitlines()]
board = list(range(1,11))
dice = list(range(1,101))

# print(f"Player 1 starting position: {position[1]}")
# print(f"Player 2 starting position: {position[2]}")

turn = 0
score = {k: 0 for k in (1, 2)}
while score[1]<1000 and score[2]<1000:
    turn += 1
    plr = (turn+1)%2+1
    roll = [dice[(turn*3)%100-3], dice[(turn*3)%100-2], dice[(turn*3)%100-1]]
    old = position[plr]
    position[plr] = board[(position[plr] + sum(roll))%10-1]
    score[plr] += position[plr]
    # print(f"Player {plr} rolls {roll} and moves to space {position[plr]} "
    #       f"for a total score of {score[plr]}.")

answer = 3 * turn * min(score.values())
print("aoc 2021 day 21 part 2:", answer)

#!python
"""advent of code 2022 day 8 part 1"""
trees = [list(map(int, line)) for line in open("input.txt").read().splitlines()]
length = len(trees)

answer = 0
for x in range(1, length-1):
    for y in range(1, length-1):
        score = [x, length-1-x, y, length-1-y]

        for n in range(x-1, -1, -1): # looking up
            if trees[x][y] <= trees[n][y]:
                score[0] = x-n
                break

        for n in range(x+1, length): # looking down
            if trees[x][y] <= trees[n][y]:
                score[1] = n-x
                break

        for n in range(y-1, -1, -1): # looking left
            if trees[x][y] <= trees[x][n]:
                score[2] = y-n
                break

        for n in range(y+1, length): # looking right
            if trees[x][y] <= trees[x][n]:
                score[3] = n-y
                break

        answer = max(answer, score[0] * score[1] * score[2] * score[3])

print("part 2:", answer)

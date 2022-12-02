#!python
"""advent of code 2022 day 2 part 1"""
rounds = [tuple(_.split()) for _ in open("input.txt").read().splitlines()]

# rock = A, X, 1
# paper = B, Y, 2
# scissors = C, Z, 3
shape_score = {
    'X': 1,
    'Y': 2,
    'Z': 3,
}

score = 0
for round in rounds:
    score += shape_score[round[-1]]
    # win
    if round in {('A', 'Y'), ('B', 'Z'), ('C', 'X')}:
        score += 6
    # draw
    if round in {('A', 'X'), ('B', 'Y'), ('C', 'Z')}:
        score += 3

print("part 1:", score)

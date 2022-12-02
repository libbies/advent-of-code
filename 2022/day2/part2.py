#!python
"""advent of code 2022 day 2 part 2"""
rounds = [tuple(_.split()) for _ in open("input.txt").read().splitlines()]

# rock = A, X, 1
# paper = B, Y, 2
# scissors = C, Z, 3
wins = {
    'A': 2,
    'B': 3,
    'C': 1,
}
draws = {
    'A': 1,
    'B': 2,
    'C': 3,
}
losses = {
    'A': 3,
    'B': 1,
    'C': 2,
}

# x: lose
# y: draw
# z: win
score = 0
for round in rounds:
    if round[-1] == 'X':
        score += 0 + losses[round[0]]
    if round[-1] == 'Y':
        score += 3 + draws[round[0]]
    if round[-1] == 'Z':
        score += 6 + wins[round[0]]

print("part 2:", score)

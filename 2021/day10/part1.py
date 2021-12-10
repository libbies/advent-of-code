"""advent of code 2021 day 10 part 1"""
lines = open("input.txt").read().splitlines()

points = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}

answer = 0
for line in lines:
    tokens = []
    for c in line:
        if not tokens or c in "([{<":
            tokens.append(c)
        elif "([{<".index(tokens[-1])==")]}>".index(c):
            tokens.pop()
        elif c in points:
            answer += points[c]
            break

print("day 10 part 1:", answer)

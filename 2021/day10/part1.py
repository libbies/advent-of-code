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
    for c in list(line):
        if not tokens:
            if c in points:
                answer += points[c]
                break
            tokens.append(c)
        elif c in "([{<":
            tokens.append(c)
        elif "([{<".index(tokens[-1])==")]}>".index(c):
            tokens.pop()
        elif c in points:
            answer += points[c]
            break
        # else:                                 # undefined

print("day 10 part 1:", answer)

"""advent of code 2021 day 10 part 2"""
lines = open("input.txt").read().splitlines()

points = {
    '(': 1,
    '[': 2,
    '{': 3,
    '<': 4,
}

scores = list()
for line in lines:
    l = list(line)
    tokens = []
    for i, c in enumerate(l):
        if not tokens:
            if c in ")]}>":
                break
            tokens.append(c)
        elif c in points:
            tokens.append(c)
        elif "([{<".index(tokens[-1])==")]}>".index(c):
            tokens.pop()
        elif c in ")]}>":
            break
        # else:                                 # undefined
    else:
        score = 0
        for c in tokens[::-1]:
            score *= 5
            score += points[c]
        scores.append(score)

answer = (len(scores), sorted(scores)[len(scores)//2])
print("day 10 part 1:", answer)

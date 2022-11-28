from itertools import groupby

inputs = open("input.txt").read().splitlines()

nice = list()
for s in inputs:
    if [bad for bad in ["ab","cd","pq","xy"] if bad in s]:
        continue
    if sum([s.count(vowel) for vowel in set("aeiou") if vowel in s]) < 3:
        continue
    if [c for c, n in groupby(s) if sum(1 for _ in n) >= 2]:
        nice.append(s)

print("part1:", len(nice))

nice = set()
for s in inputs:
    if len(s) <=3:
        continue
    for i in range(len(s)-2):
        if s.count(s[i:i+2]) >= 2:
            # print(s[i:i+2], s)
            for j in range(len(s)-2):
                if s[j] == s[j+2]:
                    # print(s[j], s[j+2], s)
                    nice.add(s)

print("part2:", len(nice))

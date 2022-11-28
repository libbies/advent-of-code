from collections import Counter as counter

words = open("input.txt").read().splitlines()

l = len(words[0])

most_common = str()
least_common = str()
for n in range(l):
    c = counter(w[n] for w in words).most_common()
    most_common += c[0][0]
    least_common += c[-1][0]

print("part1:", most_common)
print("part2:", least_common)

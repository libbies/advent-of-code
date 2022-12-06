#!python
"""advent of code 2022 day 6 part 1"""
data = open("input.txt").read().strip()

for i in range(len((data))):
    if len(set(data[i:i+4])) == 4:
        answer = i + 4
        break

print("part 1:", answer)

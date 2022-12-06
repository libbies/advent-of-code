#!python
"""advent of code 2022 day 6 part 2"""
data = open("input.txt").read().strip()

for i in range(len((data))):
    if len(set(data[i:i+14])) == 14:
        answer = i + 14
        break

print("part 2:", answer)

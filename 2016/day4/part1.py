from collections import Counter as counter

rooms = open("input.txt").read().splitlines()

def checksum(s):
    c = counter(c for c in s if c.isalpha())
    s = sorted(c.most_common(), key=lambda x: (-x[1], x[0]))
    return ''.join(x[0] for x in s[:5])

total = 0
for room in rooms:
    csum = checksum(room[:-7])
    if csum == room[-6:-1]:
        # print(room)
        total += int(room[:-7].rsplit('-', maxsplit=1)[-1])

print("part1:", total)

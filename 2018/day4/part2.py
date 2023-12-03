#!/usr/bin/env python
"""advent of code 2018 day 4 part 2"""
import re
lines = sorted(
        re.split("[^0-9A-Za-z-]", line, maxsplit=5)
        for line in open("input.txt").read().splitlines()
    )

minutes = { line[1]: [False for _ in range(61)] for line in lines }

for _, date, _, minute, _, event in lines:
    minute = int(minute)
    if "begins" in event:
        guard = event.split()[1]
    if event == "falls asleep":
        minutes[date][-1] = guard
        prev = minute
    if event == "wakes up":
        for m in range(prev, minute):
            minutes[date][m] = True

guards = {_[-1] for _ in minutes.values()}

best = 0
for minute in range(60):
    for guard in guards:
        count = sum(hour[minute] for hour in minutes.values() if hour[-1]==guard)
        if count > best:
            best, answer = count, int(guard.strip("#")) * minute

print("aoc 2018 day 4 part 2:", answer)

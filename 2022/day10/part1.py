#!python
"""advent of code 2022 day 10 part 1"""
lines = [line.split() for line in open("input.txt").read().splitlines()]

cycle = 1
registers = { "X": 1 }
answer = 0
for line in lines:
    if line[0] == "noop":
        if cycle == 20 or (cycle % 40)== 20:
            answer += cycle * registers["X"]
        cycle += 1
    elif line[0] == "addx":
        if cycle == 20 or (cycle % 40)== 20:
            answer += cycle * registers["X"]
        cycle += 1
        if cycle == 20 or (cycle % 40)== 20:
            answer += cycle * registers["X"]
        cycle += 1
        registers["X"] += int(line[-1])

print("part 1:", answer)

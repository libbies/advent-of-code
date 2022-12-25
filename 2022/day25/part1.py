#!python
"""advent of code 2022 day 25 part 1"""
numbers = [list(line) for line in open("input.txt").read().splitlines()]
snafu = {
    2: "2", "2":  2,
    1: "1", "1":  1,
    0: "0", "0":  0,
    4: "-", "-": -1,
    3: "=", "=": -2,
}

total = 0
for number in numbers:
    for i, n in enumerate(reversed(number)):
        total += snafu[n] * 5**i

answer = str()
while total:
    rem = total%5
    answer = snafu[rem] + answer
    total = (total - snafu[snafu[rem]])//5

print("part 1:", answer)

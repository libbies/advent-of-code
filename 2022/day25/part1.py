#!python
"""advent of code 2022 day 25 part 1"""
numbers = [list(line) for line in open("input.txt").read().splitlines()]

def calc(number):
    answer = 0
    for i, n in enumerate(reversed(number)):
        if n.isnumeric():
            answer += (5**i) * int(n)
        elif n=="-":
            answer += (5**i) * -1
        elif n=="=":
            answer += (5**i) * -2
    return answer

total = 0
for number in numbers:
    total += calc(number)

snafu = {2: "2", 1: "1", 0: "0", 4: "-", 3: "="}

answer = str()
while total:
    rem = total%5
    answer = snafu[rem] + answer
    total = (total + (-rem if rem<=2 else 5-rem))//5

print("part 1:", answer)

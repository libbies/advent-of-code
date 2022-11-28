"""advent of code 2015 day 11 part 1"""
import string

password = open("input.txt").read().strip()

def pw2int(pw):
    n = 0
    for i, c in enumerate(pw[::-1]):
        n += 26**i * (ord(c)-97)
    return n

def int2pw(n):
    pw = list()
    while n:
        digit, n = chr(n%26+97), n//26
        pw.append(digit)
    return ''.join(pw[::-1])

runs = [''.join(_) for _ in zip(string.ascii_lowercase,
                                string.ascii_lowercase[1:],
                                string.ascii_lowercase[2:])]

pwd = pw2int(password)
while pwd:
    pwd += 1
    answer = int2pw(pwd)
    if 'i' in answer or 'o' in answer or 'l' in answer:
        continue
    if len({_ for _ in zip(answer, answer[1:]) if _[0]==_[1]})<2:
        continue
    if any(run for run in runs if run in answer):
        break

print("aoc 2015 day 11 part 1:", answer)

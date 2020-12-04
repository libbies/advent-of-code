#!/usr/bin/env python3

lines = map(str.split, open("input.txt", 'r').readlines())

valid = 0
for (count, char, password) in lines:
    c1, c2 = sorted(map(int, count.split('-')))
    if c1 <= password.count(char[0]) <= c2:
        valid += 1

print(valid)

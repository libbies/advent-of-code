#!/usr/bin/env python3

lines = map(str.split, open("input.txt", 'r').readlines())

valid = 0
for (locations, char, password) in lines:
    loc1, loc2 = map(int, locations.split('-'))
    if (password[loc1-1]==char[0]) ^ (password[loc2-1]==char[0]):
        valid += 1

print(valid)

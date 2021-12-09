#!/usr/bin/env python3
from itertools import combinations

with open("input.txt", "r") as f:
    expenses = map(int, f.readlines())
    result = [c for c in combinations(expenses, 2) if sum(c) == 2020]
    print(f"{result} = {result[0][0] * result[0][1]}")

#!/usr/bin/env python3
"""advent of code 2024 day 7 part 2"""

answer = 0
for line in open("input.txt").read().splitlines():
    test, values = line.split(':', maxsplit=1)
    test = int(test)
    values = [int(_) for _ in values.split()]
    results = [values.pop(0)]
    while values:
        n = values.pop(0)
        results = [v*n for v in results if v*n<=test] \
            + [v+n for v in results if v+n<=test] \
            + [int(str(v)+str(n)) for v in results]
    if test in results:
        answer += test

print("aoc 2024 day 7 part 2:", answer)

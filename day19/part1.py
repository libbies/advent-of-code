from itertools import product
from functools import lru_cache

lines = open("input.txt").read().splitlines()

rules = {
    k: [*map(str.split, v.split(' | '))]
    for k,v in (
        r.split(': ')
        for r in (l for l in lines if l and l[0].isdigit())
    )
}

messages = (l for l in lines if l and l.isalpha())

@lru_cache(maxsize=len(rules))
def evaluate(n):
    """evaluate rule n"""
    if rules[n] == [['"a"']]:
        return ["a"]
    elif rules[n] == [['"b"']]:
        return ["b"]
    else:
        candidates = list()
        for rule in rules[n]:
            e = (evaluate(r) for r in rule)
            candidates.extend(''.join(p) for p in product(*e))
    return candidates

valid = evaluate("0")

print("part1:", len([msg for msg in messages if msg in valid]))

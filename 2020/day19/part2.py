import re
from pprint import pprint
from functools import cache

lines = open("input.txt").read().splitlines()

rules = {
    k: [*map(str.split, v.split(' | '))]
    for k,v in (
        r.split(': ')
        for r in (l for l in lines if l and l[0].isdigit())
    )
}

messages = [l for l in lines if l and l.isalpha()]

@cache
def evaluate(n):
    """evaluate rule n"""
    if n not in rules.keys():
        raise(StopIteration)
    # print(f"rules[{n}]:", rules[n])
    if rules[n] == [['"a"']]:
        return "a"
    elif rules[n] == [['"b"']]:
        return "b"
    else:
        candidates = list()
        for rule in rules[n]:
            e = [evaluate(r) for r in rule if r!=n]
            # print("e:", e)
            candidates += [''.join(e)]
            if n in rule:
                # print("loop:", rule, n)
                if len(e) == 1:
                    candidates = ["(" + c + ")+" for c in candidates]
                else:
                    candidates = [
                        "(" + e[0] + "{" + str(n) + "}" + e[1] + "{" + str(n) + "}" + ")"
                        for n in range(1, 6) # magic number derived via trial and error
                    ]
                # pprint(candidates)
        candidates = '(' + '|'.join(candidates) + ')'
        # print("+:", n, candidates)
    return candidates

valid = re.compile('^' + evaluate("0") + '$')
print("part1:", len([msg for msg in messages if re.match(valid, msg)]))

rules["8"] = [['42'], ['42', '8']]
rules["11"] = [['42', '31'], ['42', '11', '31']]

evaluate.cache_clear()
valid = re.compile('^' + evaluate("0") + '$')
print("part2:", len([msg for msg in messages if re.match(valid, msg)]))

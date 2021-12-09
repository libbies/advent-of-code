"""advent of code 2021 day 8 part 2"""
patterns = [_.split() for _ in open("input.txt").read().splitlines()]

mapping = {            # len()
    0: set("abcefg"),  # 6
    1: set("cf"),      # 2
    2: set("acdeg"),   # 5
    3: set("acdfg"),   # 5
    4: set("bcdf"),    # 4
    5: set("abdfg"),   # 5
    6: set("abdefg"),  # 6
    7: set("acf"),     # 3
    8: set("abcdefg"), # 7
    9: set("abcdfg"),  # 6
}

for i, row in enumerate(patterns):
    mapping = dict()

    # first pass for 1, 4, 7, 8
    for j, p in enumerate(row):
        if len(p)==2:
            mapping[1]=p
            patterns[i][j] = "1"
        elif len(p)==3:
            mapping[7]=p
            patterns[i][j] = "7"
        elif len(p)==4:
            mapping[4]=p
            patterns[i][j] = "4"
        elif len(p)==7:
            patterns[i][j] = "8"

    # second pass for 7->3, 4->9
    for j, p in enumerate(row):
        if len(p)==5 and all(_ in p for _ in mapping[7]):
            patterns[i][j] = "3"
        elif all(_ in p for _ in mapping[4]):
            patterns[i][j] = "9"

    # third pass for 1->0
    for j, p in enumerate(row):
        if all(_ in p for _ in mapping[1]):
            patterns[i][j] = "0"

    # fourth pass for 6
    for j, p in enumerate(row):
        if len(p)==6:
            mapping[6]=p
            patterns[i][j] = "6"

    # fifth pass for 6-->5
    for j, p in enumerate(row):
        if all(_ in mapping[6] for _ in p):
            patterns[i][j] = "5"

    # last pass for 2
    for j, p in enumerate(row):
        if len(p)==5:
            patterns[i][j] = "2"

# pprint([''.join(_) for _ in patterns][-10:])

answer = sum(int(''.join(line[-4:])) for line in patterns)
print("part 2 answer:", answer)

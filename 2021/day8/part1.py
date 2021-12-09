"""advent of code 2021 day 8 part 1"""
inputs = [_.split('|') for _ in open("input.txt").read().splitlines()]

outputs = [_[-1].split() for _ in inputs]

##############
# 0: abc efg # 6
# 1:   c  f  # 2 <--
# 2: a cde g # 5
# 3: a cd fg # 5
# 4:  bcd f  # 4 <--
# 5: ab d fg # 5
# 6: ab defg # 6
# 7: a c  f  # 3 <--
# 8: abcdefg # 7 <--
# 9: abcd fg # 6
##############

answer = 0
for i, row in enumerate(outputs):
    for j, p in enumerate(row):
        if len(p) in [2, 4, 3, 7]:
            answer += 1

print("part 1 answer:", answer)

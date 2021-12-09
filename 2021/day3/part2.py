"""advent of code 2021 day 3 part 2"""
from collections import Counter

inputs = open("input.txt").read().splitlines()

o2_candidates = list(inputs)
co_candidates = list(inputs)
for i in range(len(inputs[0])):
    o2_ctr = Counter(_[i] for _ in o2_candidates)
    co_ctr = Counter(_[i] for _ in co_candidates)
    max_o2 = '1' if o2_ctr['1']==o2_ctr['0'] else o2_ctr.most_common()[0][0]
    min_co = '0' if co_ctr['0']==co_ctr['1'] else co_ctr.most_common()[-1][0]
    o2_candidates = [_ for _ in o2_candidates if _[i]==max_o2]
    co_candidates = [_ for _ in co_candidates if _[i]==min_co]

answer = int("0b"+''.join(o2_candidates[0]), 2) \
            * int("0b"+''.join(co_candidates[0]), 2)
print("part 2 answer:", answer)

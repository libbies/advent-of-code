#!python
# cython: language_level=3
"""advent of code 2017 day 3 part 1"""

num = "368078"

# solved by hand in numbers
# 606 * 607 = 367842
# 368078 - 367842 = 236
answer = 606 + 1 - 236

print("part 1: {}".format(answer))

"""advent of code 2021 day 1 part 1"""
nums = (int(_) for _ in open("input.txt").readlines())

last = next(nums)
inc = 0
for n in nums:
    if n>last:
        inc += 1
    last = n

print("part 1:", inc)

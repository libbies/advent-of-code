#!/usr/bin/env python3

count = 0
for p in range(125730, 579381):
    nums = [int(n) for n in str(p)]
    if len(nums) == len(set(nums)):
        continue
    if nums != sorted(nums):
        continue
    if nums[0] == nums[1] or nums[1] == nums[2] or nums[2] == nums[3] or nums[3] == nums[4] or nums[4] == nums[5]:
        count += 1

print(count)

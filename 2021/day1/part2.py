"""advent of code 2021 day 1 part 2"""
nums = (int(_) for _ in open("input.txt").readlines())

inc = 0
win = [next(nums), next(nums), next(nums)]
for n in nums:
    last = sum(win)
    win.pop(0)
    win.append(n)
    if last<sum(win):
        inc += 1
    # print(win, n, last, sum(win), inc)

print("part 2:", inc)

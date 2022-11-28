from _md5 import md5 # faster than hashlib.md5 for <512 bytes

def calc_ud(s):
    return s.count('D') - s.count('U')

def calc_lr(s):
    return s.count('R') - s.count('L')

passcode = open("input.txt").read().strip()
unlocked = set("bcdef")
paths = ['']
solutions = list()
while paths:
    path = paths.pop(0)
    if 3 == calc_ud(path) == calc_lr(path):
        solutions.append(path)
        continue
    doors = md5(f"{passcode}{path}".encode()).hexdigest()[:4]
    if doors[0] in unlocked and calc_ud(path) > 0:
        paths.append(path + 'U')
    if doors[1] in unlocked and calc_ud(path) < 3:
        paths.append(path + 'D')
    if doors[2] in unlocked and calc_lr(path) > 0:
        paths.append(path + 'L')
    if doors[3] in unlocked and calc_lr(path) < 3:
        paths.append(path + 'R')

print("solutions:", len(solutions), "part2:", max(len(s) for s in solutions))

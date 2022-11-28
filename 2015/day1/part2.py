input = open("input.txt").read().strip()

floor = 0
for i, c in enumerate(input):
    if c=='(':
        floor += 1
    if c==')':
        floor -= 1
    if floor==-1:
        print(i+1)
        break

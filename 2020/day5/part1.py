passes = [l.strip() for l in open("input.txt").readlines()]

seats = dict()
for p in passes:
    row, row_max = 0, 128
    for s in [c for c in p][:-3]:
        if s=='F':
            row_max = (row_max+row)//2
        elif s=='B':
            row = (row+row_max)//2
    col, col_max = 0, 8
    for s in [c for c in p][7:]:
        if s=='L':
            col_max = (col_max+col)//2
        elif s=='R':
            col = (col+col_max)//2
    seats[p] = row*8+col

print(sorted(seats.items(), key=lambda x: x[1])[-5:])

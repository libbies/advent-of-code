passes = [l.strip() for l in open("input.txt").readlines()]

seats = dict()
for p in passes:
    row_min, row, row_max = 0, 64, 128
    for s in [c for c in p][:-3]:
        if s=='F':
            row_max, row = row, (row_min+row)//2
        elif s=='B':
            row_min, row = row, (row_max+row)//2
    col_min, col, col_max = 0, 4, 8
    for s in [c for c in p][7:]:
        if s=='L':
            col_max, col = col, (col_min+col)//2
        elif s=='R':
            col_min, col = col, (col_max+col)//2
    seats[p] = row*8+col

seat = [*set(range(min(seats.values()), max(seats.values())))
        -set(seats.values())][0]

print(f"[{seat}]"
      f" between {[p for p in seats if seats[p]==seat-1]}"
      f" and {[p for p in seats if seats[p]==seat+1]}")

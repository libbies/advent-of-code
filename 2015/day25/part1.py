input = [
    int(n) for n in ''.join([
        c for c in open("input.txt").read() if c.isdigit() or c.isspace()
    ]).split()
]

n, prev = 3, 20151125
while n <= (input[0] + input[1]):
    x = n
    y = n - x
    while y != n - 1:
        x -= 1
        y += 1
        prev = divmod(prev * 252533, 33554393)[-1]
        if input[0] == x and input[1] == y:
            print(x, y, prev)
    n += 1

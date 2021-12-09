"""advent of code 2021 day 7 part 2"""
positions = [int(_) for _ in open("bigint.txt").read().split(',')]

def fuel(distance):
    """fuel cost is just a triangular number, lol"""
    return distance*(distance+1)//2

answer = min(
    sum(fuel(abs(p-n)) for p in positions)
    for n in range(max(positions))
)

print("part 2 answer:", answer)

from functools import lru_cache

@lru_cache(1)
def recurse(iterations):
    if iterations == 0:
        return 1
    return 7 * recurse(iterations - 1) % 20201227

def transform(sn, iterations):
    result = 1
    for n in range(iterations):
        result = sn * result % 20201227
    return result

card_pub_key, door_pub_key = map(int, open("input.txt").read().splitlines())
key = 1
for loop in range(1, door_pub_key):
    # key = recurse(loop)
    key = 7 * key % 20201227
    if key == card_pub_key:
        print("card loop:", loop, "part1:", transform(door_pub_key, loop))
        break
    if key == door_pub_key:
        print("door loop:", loop, "part1:", transform(card_pub_key, loop))
        break

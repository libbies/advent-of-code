import hashlib

input = b"bgvyzdsv"

hash = hashlib.md5(input)
for n in range(10000000):
    key = hash.copy()
    key.update(str.encode(str(n)))
    if key.hexdigest().startswith("000000"):
        print("part2:", n, key.hexdigest())
        break
    elif key.hexdigest().startswith("00000"):
        print("part1:", n, key.hexdigest())

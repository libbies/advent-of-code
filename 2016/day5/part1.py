from hashlib import md5

id = open("input.txt", "r+b").read().strip()

base = md5(id)

n = 0
password = str()
while len(password) < 8:
    hash = base.copy()
    hash.update(f"{n}".encode())
    if hash.hexdigest().startswith("00000"):
        print(n, hash.hexdigest())
        password += hash.hexdigest()[5]
    n += 1

print("part1:", password)

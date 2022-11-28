from hashlib import md5

id = open("input.txt", "r+b").read().strip()

base = md5(id)

n = 0
password = ['_'] * 8
while '_' in password:
    hash = base.copy()
    hash.update(f"{n}".encode())
    if hash.hexdigest().startswith("00000"):
        pos = hash.hexdigest()[5]
        if pos.isdigit() and 0 <= int(pos) <= 7 and password[int(pos)] == '_':
            password[int(pos)] = hash.hexdigest()[6]
            print(n, hash.hexdigest(), pos, ''.join(password))
    n += 1

print("part2:", ''.join(password))

from hashlib import md5
from hashlib import pbkdf2_hmac

salt = open("input.txt").read().strip()

threes = [c*3 for c in '0123456789abcdef']

hashes = dict()
keys = list()

block = 0
size = 1000
while len(keys) < 64:
    for n in range(block, block+size+size):
        tmp = md5(f"{salt}{n}".encode()).hexdigest()
        for _ in range(2016):
            tmp = md5(tmp.encode()).hexdigest()
        hashes[n] = tmp
    for n in range(block, block+size):
        candidates = [sub for sub in threes if sub in hashes[n]]
        fives = [(hashes[n].index(c), c) for c in candidates]
        if fives:
            five = sorted(fives)[0][-1][0] * 5
            key = next((
                (n, n+offset, hashes[n+offset])
                for offset in range(1, size+1)
                if five in hashes[n+offset]
            ), None)
            if key:
                keys.append(key)
                if len(keys) <= 5 or len(keys) >= 60:
                    print(len(keys), five, key)
    block += size

print('\n' + "part1:", keys[63][0])

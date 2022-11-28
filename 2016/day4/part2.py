from collections import Counter as counter

rooms = open("input.txt").read().splitlines()

def checksum(s):
    c = counter(c for c in s if c.isalpha())
    s = sorted(c.most_common(), key=lambda x: (-x[1], x[0]))
    return ''.join(x[0] for x in s[:5])

def shift(s, n):
    ciphertext = ''.join(c for c in s)
    plaintext = str()
    for c in ciphertext:
        if c.isalpha() and chr(ord(c) + n).isalpha():
            plaintext += chr(ord(c) + n)
        elif c.isalpha() and chr(ord(c) + n - 26).isalpha():
            plaintext += chr(ord(c) + n - 26)
        else:
            plaintext += c
    return plaintext

total = 0
for room in rooms:
    csum = checksum(room[:-7])
    if csum == room[-6:-1]:
        key = int(room[:-7].rsplit('-', maxsplit=1)[-1]) % 26
        # print(shift(room[:-7], key), key)
        if 'northpole' in shift(room[:-7], key):
            print(shift(room[:-7], key), "part2:",
                        room[:-7].rsplit('-', maxsplit=1)[-1])

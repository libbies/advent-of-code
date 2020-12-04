passports=list()
lines = [*map(str.split, open("example-valid.txt").read().split('\n\n'))]
passports = [{l.split(':')[0]: l.split(':')[1]  for l in line} for line in lines]

valid=0
for p in passports:
    print(p)
    # minimum fields
    if len(p)<7:
        print('die1')
        continue
    # cid (Country ID) - ignored, missing or not.
    if len(p)<8 and "cid" in passport:
        print(len(p))
        print('die2')
        continue
    # byr (Birth Year) - four digits; at least 1920 and at most 2002.
    if not 1920 <= int(p["byr"]) <= 2002:
        print('die3')
        continue
    # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    if not 2010 <= int(p["iyr"]) <= 2020:
        print('die4')
        continue
    # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    if not 2020 <= int(p["eyr"]) <= 2030:
        print('die5')
        continue
    # hgt (Height) - a number followed by either cm or in:
    if not (p["hgt"].endswith("cm") or p["hgt"].endswith("in")):
        print('die6')
        continue
    # If cm, the number must be at least 150 and at most 193.
    if p["hgt"].endswith("cm") and not 150 <= int(p["hgt"][:-2]) <= 193:
        print('die7')
        continue
    # If in, the number must be at least 59 and at most 76.
    if p["hgt"].endswith("in") and not 59 <= int(p["hgt"][:-2]) <= 76:
        print('die8')
        continue
    # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    if len(p["hcl"])!=7 or not p["hcl"].startswith("#"):
        print('die9')
        continue
    if len([*filter(lambda c: c in "0123456789abcdef", p["hcl"][1:])]) != 6:
        print('die10')
        continue
    # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    if not (p["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "ath"]):
        print('die11')
        continue
    # pid (Passport ID) - a nine-digit number, including leading zeroes.
    if len(p["pid"]) != 9 or not p["pid"].isdigit():
        print('die12')
        continue
    valid += 1

print(valid)

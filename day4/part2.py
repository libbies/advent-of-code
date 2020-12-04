passports=list()
lines = [*map(str.split, open("input.txt").read().split('\n\n'))]
passports = [{l.split(':')[0]: l.split(':')[1]  for l in line} for line in lines]

valid=0
for p in passports:
    # minimum fields
    if len(p)<7:
        continue
    # cid (Country ID) - ignored, missing or not.
    if len(p)<8 and "cid" in p:
        continue
    # byr (Birth Year) - four digits; at least 1920 and at most 2002.
    if not 1920 <= int(p["byr"]) <= 2002:
        continue
    # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    if not 2010 <= int(p["iyr"]) <= 2020:
        continue
    # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    if not 2020 <= int(p["eyr"]) <= 2030:
        continue
    # hgt (Height) - a number followed by either cm or in:
    if not (p["hgt"].endswith("cm") or p["hgt"].endswith("in")):
        continue
    # If cm, the number must be at least 150 and at most 193.
    if p["hgt"].endswith("cm") and not 150 <= int(p["hgt"][:-2]) <= 193:
        continue
    # If in, the number must be at least 59 and at most 76.
    if p["hgt"].endswith("in") and not 59 <= int(p["hgt"][:-2]) <= 76:
        continue
    # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    if (len(p["hcl"])!=7 or not p["hcl"].startswith("#")
            and len([*filter(lambda c: c in "0123456789abcdef", p["hcl"][1:])]) != 6):
        continue
    # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    if not (p["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]):
        continue
    # pid (Passport ID) - a nine-digit number, including leading zeroes.
    if len(p["pid"]) != 9 or not p["pid"].isdigit():
        continue
    valid += 1

print(valid)

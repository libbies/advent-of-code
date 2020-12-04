print(len([
    p for p in [
        {l.split(':')[0]: l.split(':')[1]  for l in line}
        for line in [*map(str.split, open("input.txt").read().split('\n\n'))]
    ]
    if len(p)>=7
    if len(p)>=8 or "cid" not in p
    if 1920 <= int(p["byr"]) <= 2002
    if 2010 <= int(p["iyr"]) <= 2020
    if 2020 <= int(p["eyr"]) <= 2030
    if p["hgt"].endswith("cm") or p["hgt"].endswith("in")
    if not(p["hgt"].endswith("cm") and not 150 <= int(p["hgt"][:-2]) <= 193)
    if not(p["hgt"].endswith("in") and not 59 <= int(p["hgt"][:-2]) <= 76)
    if len(p["hcl"])==7
    if p["hcl"].startswith("#")
    if len([*filter(lambda c: c in "0123456789abcdef", p["hcl"][1:])])==6
    if p["ecl"] in ["amb","blu","brn","gry","grn","hzl","oth"]
    if len(p["pid"])==9
    if p["pid"].isdigit()
]))

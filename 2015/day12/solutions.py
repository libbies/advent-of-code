import re
import json
raw_data = open("input.txt").read().strip()

print("part1:", sum(map(int, re.findall('-?\d+', raw_data))))

json_data = json.loads(raw_data)

def recurse(obj):
    if type(obj)==dict and "red" not in obj.values():
        return sum(recurse(o) for o in obj.values())
    elif type(obj)==list:
        return sum(recurse(o) for o in obj)
    elif type(obj)==int:
        return obj
    return 0

print("part2:", recurse(json_data))

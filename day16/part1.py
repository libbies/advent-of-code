from functools import cache

def ticket_rate(ticket):
    for t in ticket:
        for rule in rules:
            if rule[0] <= t <= rule[1]:
                break
        else: # did not match a rule:
            return t
    return 0

lines = open("input.txt").read().splitlines()

rules = [[*map(int, r.split('-'))] for l in lines if ":" in l for r in l.split() if '-' in r]

tickets = [[*map(int, l.split(','))] for l in lines if ',' in l]

rate = 0
for ticket in tickets[1:]:
    rate += ticket_rate(ticket)

print("part1:", rate)

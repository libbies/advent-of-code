from functools import cache

def check_ticket(ticket):
    for t in ticket:
        for r0, r1 in [r for rule in rules.values() for r in rule]:
            if r0 <= t <= r1:
                break
        else: # did not match a rule:
            return False
    return True

lines = open("input.txt").read().splitlines()

rules = dict()
for l in lines:
    if ':' in l and 'ticket' not in l:
        name, rule = l.split(': ')
        rules[name] = [[*map(int, r.split('-'))] for r in rule.split(' or ')]

tickets = [[*map(int, l.split(','))] for l in lines if ',' in l]

valid_tickets = list()
for ticket in tickets[1:]:
    if check_ticket(ticket):
        valid_tickets.append(ticket)

queue = [*range(len(rules))]
order = [ None ] * len(rules)
while queue:
    field = queue[0]
    candidates = list()
    for name, rule in rules.items():
        if name in order:
            continue
        matches = [
            (n, r)
            for n in [t[field] for t in valid_tickets]
            for r in rule if r[0]<=n<=r[1]
        ]
        if len(matches) == len(valid_tickets):
            candidates.append(name)
    # print(field, candidates)
    queue.remove(field)
    if len(candidates) == 1:
        order[field] = candidates[0]
    else:
        queue.append(field)

total = 1
for i, field in enumerate(order):
    if field.startswith("departure"):
        print(field, tickets[0][i])
        total *= tickets[0][i]

print("part2:", total)

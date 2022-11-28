def combat(player_armor, player_damage):
    player_hp = 100
    boss_hp, boss_damage, boss_armor = boss.values()
    turn = 1
    while player_hp > 0 and boss_hp > 0:
        if turn % 2 == 1: # player's turn
            boss_hp -= max(1, player_damage - boss_armor)
        else:
            player_hp -= max(1, boss_damage - player_armor)
        turn += 1
    return (player_hp, boss_hp)

items = [l.rsplit(maxsplit=3) for l in open("itemshop.txt").read().splitlines()]

weapons = {l[0]: [int(i) for i in l[-3:]] for l in items[1:6]}
armor = {l[0]: [int(i) for i in l[-3:]] for l in items[8:13]}
rings = {l[0]: [int(i) for i in l[-3:]] for l in items[15:]}

armor['optional'] = [0, 0, 0]
rings['optional_r1'] = [0, 0, 0]
rings['optional_r2'] = [0, 0, 0]
maximum = (max(w[0] for w in weapons.values())
         + max(a[0] for a in armor.values())
         + max(r[0] for r in rings.values()) * 2)

boss = dict()
for l in open("input.txt").read().splitlines():
    l = l.split(": ")
    boss[l[0]] = int(l[1])

COST = 0
DAMAGE = 1
ARMOR = 2
for w in weapons.values():
    for a in armor.values():
        for r1 in rings.values():
            for r2 in rings.values():
                cost = w[COST] + a[COST] + r1[COST] + r2[COST]
                if r1 == r2:
                    continue
                elif cost >= maximum:
                    continue
                player_hp, boss_hp = combat(
                        player_damage=sum(i[DAMAGE] for i in (w,a,r1,r2)),
                        player_armor=sum(i[ARMOR] for i in (w,a,r1,r2)))
                if player_hp > boss_hp:
                    print("win:", cost, (player_hp, boss_hp), w, a, r1, r2)
                    maximum = cost

print("part1:", maximum)

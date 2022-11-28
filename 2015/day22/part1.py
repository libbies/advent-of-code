boss = {
    stat: int(value)
    for (stat, value) in (
        l.split(': ') for l in open("input.txt").read().splitlines()
    )
}

class Timer():
    def __init__(self, shield=0, poison=0, recharge=0):
        self.shield = shield
        self.poison = poison
        self.recharge = recharge
    def decrement(self):
        self.shield = max(0, self.shield - 1)
        self.poison = max(0, self.poison - 1)
        self.recharge = max(0, self.recharge - 1)
    def copy(self):
        timer = Timer(self.shield, self.poison, self.recharge)
        return timer

class State():
    def __init__(self, boss_hp, boss_dmg, player_hp=50, mana=500, spent=0, timers=None):
        self.boss_hp = boss_hp
        self.boss_dmg = boss_dmg
        self.player_hp = player_hp
        self.mana = mana
        self.spent = spent
        self.timers = timers if timers else Timer()
    def repr(self):
        print(f"boss: {self.boss_hp}, player: {self.player_hp}, mana: {self.spent}/{self.mana}")
    def copy(self):
        new_state = State(self.boss_hp, self.boss_dmg, self.player_hp,
                          self.mana, self.spent, self.timers.copy())
        return new_state

spells = {
    "magic": 53,
    "drain": 73,
    "shield": 113,
    "poison": 173,
    "recharge": 229,
}

base_state = State(boss_hp=boss["Hit Points"], boss_dmg=boss["Damage"])

game_states = [ base_state ]
minimum = 2<<15
turn = 0
while game_states:
    tmp = list()
    turn += 1
    for player_state in game_states:
        for spell in spells:
            state = player_state.copy()
            # proc effects for player turn
            if state.timers.poison:
                state.boss_hp -= 3
                if state.boss_hp <= 0:
                    state.repr()
                    if minimum > state.spent:
                        minimum = state.spent
                    continue
            if state.timers.recharge:
                state.mana += 101
            state.timers.decrement()
            # calc player mana
            if spells[spell] > state.mana:
                continue
            state.spent += spells[spell]
            state.mana -= spells[spell]
            if state.spent >= minimum:
                continue
            # proc player spell
            if spell == "magic":
                state.boss_hp -= 4
            elif spell == "drain":
                state.boss_hp -= 2
                state.player_hp += 2
            elif spell == "shield":
                if state.timers.shield > 2:
                    continue
                state.timers.shield += 6
            elif spell == "poison":
                if state.timers.poison > 2:
                    continue
                state.timers.poison += 6
            elif spell == "recharge":
                if state.timers.recharge > 2:
                    continue
                state.timers.recharge += 5
            if state.boss_hp <= 0:
                state.repr()
                if minimum > state.spent:
                    minimum = state.spent
                continue
            # end player turn
            # proc effects for boss turn
            if state.timers.poison:
                state.boss_hp -= 3
                if state.boss_hp <= 0:
                    state.repr()
                    if minimum > state.spent:
                        minimum = state.spent
                    continue
            if state.timers.recharge:
                state.mana += 101
            if state.boss_hp <= 0:
                state.repr()
                if minimum > state.spent:
                    minimum = state.spent
                continue
            if state.timers.shield:
                state.player_hp -= max(1, state.boss_dmg - 7)
            else:
                state.player_hp -= state.boss_dmg
            if state.player_hp <= 0:
                continue
            state.timers.decrement()
            # end boss turn
            tmp.append(state)
    game_states = tmp
    print("turn", turn, "len:", len(game_states), "min:", minimum)

print("part1:", minimum)

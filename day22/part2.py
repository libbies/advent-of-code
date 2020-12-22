P1 = "Player 1"
P2 = "Player 2"

decks = {
    l.split(':')[0]: [*map(int, l.split(':')[1].split())]
    for l in open("input.txt").read().split('\n\n')
}

def score(l):
    return sum((x*y for x,y in [*zip(l, reversed(range(1, len(l)+1)))]))

game = 1
def recurse(decks):
    global game
    g = int(game)
    history = {
        P1: list(),
        P2: list(),
    }
    round = 1
    while decks[P1] and decks[P2]:
        # print(f"-- Round {round} (Game {g}) --")
        # print(f"P1's deck: {decks[P1]}")
        # print(f"P1's deck: {decks[P2]}")
        # print(f"P1 plays {decks[P1][0]}")
        # print(f"P2 plays {decks[P2][0]}")
        if decks[P1] in history[P1] and decks[P2] in history[P2]:
            return P1
        history[P1].append(list(decks[P1]))
        history[P2].append(list(decks[P2]))
        c1 = decks[P1].pop(0)
        c2 = decks[P2].pop(0)
        winner = None
        if len(decks[P1]) >= c1 and len(decks[P2]) >= c2:
            game += 1
            # print(f"=== Game {game} ===")
            winner = recurse({
                P1: decks[P1][:c1],
                P2: decks[P2][:c2],
            })
        if winner == P1 or (c1 > c2 and not winner):
            winner = P1
            decks[P1].append(c1)
            decks[P1].append(c2)
        elif winner == P2 or (c2 > c1 and not winner):
            winner = P2
            decks[P2].append(c2)
            decks[P2].append(c1)
        # print(f"{winner} wins round {round} of game {g}!")
        round += 1
    if g%100 == 0:
        print(f"The winner of game {g} is {winner}!")
    if g == 1:
        print(f"part2: {score(decks[P1]) + score(decks[P2])}")
    return winner

recurse(decks)

# code.interact(local=dict(globals(), **locals()))

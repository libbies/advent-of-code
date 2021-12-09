P1 = "Player 1"
P2 = "Player 2"

decks = {
    l.split(':')[0]: [*map(int, l.split(':')[1].split())]
    for l in open("input.txt").read().split('\n\n')
}

while decks[P1] and decks[P2]:
    c1 = decks[P1].pop(0)
    c2 = decks[P2].pop(0)
    if c1 > c2:
        decks[P1].append(c1)
        decks[P1].append(c2)
    if c2 > c1:
        decks[P2].append(c2)
        decks[P2].append(c1)

print("part1:", sum([x*y for x,y in [*zip(decks[P1], reversed(range(1,len(decks[P1])+1)))]])
              + sum([x*y for x,y in [*zip(decks[P2], reversed(range(1,len(decks[P2])+1)))]]))

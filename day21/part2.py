lines = open("input.txt").read().splitlines()

foods = dict()
for line in lines:
    ingredients, allergens = line.split(' (')
    foods[ingredients] = allergens.strip(')').split(' ', maxsplit=1)[1:][-1].split(', ')

allergens = dict()
queue = list({a for allergens in foods.values() for a in allergens})
while queue:
    allergen = queue.pop(0)
    candidates = [
        [i for i in k.split() if i not in allergens.values()]
        for k, v in foods.items()
        if allergen in v
    ]
    # print(allergen, candidates)
    if len(candidates) == 1:
        if len(candidates[0]) == 1:
            allergens[allergen] = candidates[0][0]
    elif len(candidates) > 1:
        candidate = set.intersection(*[set(i) for i in candidates])
        if len(candidate) == 1:
            allergens[allergen] = next(iter(candidate))
        else:
            queue.append(allergen)
    else:
        queue.append(allergen)

safe = list()
for ingredients in foods.keys():
    for ingredient in ingredients.split():
        if ingredient not in {i for i in allergens.values()}:
            safe.append(ingredient)

print("part1:", len(safe))

print("part2:", ','.join([x[1] for x in sorted(allergens.items(), key=lambda x: x[0])]))

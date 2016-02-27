inp = {
    "American": ["burger", "french fries", "potato chips"],
    "Italian": ["pizza", "bread sticks", "potato chips"]
}

indexed = {}

for restaurant in inp.keys():
    meals = inp[restaurant]
    for meal in meals:
        if meal in indexed:
            indexed[meal] += 1
        else:
            indexed[meal] = 1

search = raw_input()

print indexed[search]

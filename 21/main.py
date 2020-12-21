
if __name__ == '__main__':
    alg_ing_set = {}
    all_ing_set = set()
    ing_list = []
    alg_list = []

    fin = open("input.txt")
    for line in fin:
        line = line.strip()
        if '(' in line:
            ingredients, allergens = line[:-1].split(" (contains ")
        else:
            ingredients, allergens = line, ""
        ingredients = ingredients.split(" ")
        ing_list.append(ingredients)
        allergens = allergens.split(", ")
        alg_list.append(allergens)

        ing_set = set(ingredients)
        all_ing_set |= ing_set
        
        for alg in allergens:
            if alg not in alg_ing_set:
                alg_ing_set[alg] = set(ingredients)
            else:
                alg_ing_set[alg] &= set(ingredients) 
    fin.close()

    # Part 1
    count = 0
    non_alg_ings = all_ing_set.copy()
    for alg in alg_ing_set:
        non_alg_ings -= alg_ing_set[alg]
    for ingredients in ing_list:
        for ing in ingredients:
            if ing in non_alg_ings:
                count += 1
    print(count)

    # Part 2
    alg_ing_map = {}
    while not all([not ing_set for ing_set in alg_ing_set.values()]):
        only_choice_algs = [alg for alg in alg_ing_set if len(alg_ing_set[alg]) == 1]
        for alg in only_choice_algs:
            ing = list(alg_ing_set[alg])[0]
            alg_ing_map[alg] = ing
            for ing_set in alg_ing_set.values():
                if ing in ing_set:
                    ing_set.remove(ing)
    sorted_by_alg = sorted(alg_ing_map.items(), key=lambda p: p[0])
    res = ",".join([ing for _, ing in sorted_by_alg])
    print(res)
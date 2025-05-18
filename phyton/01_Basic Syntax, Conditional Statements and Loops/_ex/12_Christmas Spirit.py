q_decoration = int(input())
days_to_Christmas = int(input())

pr_ornament_set = 2
points_ornament_set = 5

pr_tree_skirt = 5
points_tree_skirt = 3

pr_tree_garland = 3
points_tree_garland = 10

pr_tree_lights = 15
points_tree_lights = 17

total_cost = 0
total_spirit = 0
n_ornament_set = 0
for days in range(1, days_to_Christmas + 1):
    if days % 11 == 0:
        q_decoration += 2
    # print(f"q_decoration + {q_decoration} ")
    if days % 2 == 0:
        total_cost += pr_ornament_set * q_decoration
        total_spirit += points_ornament_set
        n_ornament_set += 1
        # total_spirit += 5

    if days % 3 == 0:
        total_cost += (pr_tree_skirt + pr_tree_garland) * q_decoration
        total_spirit += points_tree_skirt + points_tree_garland
        # total_spirit += 3 + 10

    if days % 5 == 0:
        total_cost += pr_tree_lights * q_decoration
        total_spirit += points_tree_lights
        # total_spirit += 17
        if days % 3 == 0:
            total_spirit += 30

    # if days % 2 == 0 and days % 5 == 0:
    if days % 2 == 0 and days % 5 == 0 :
        total_spirit -= 20
        total_cost += (pr_tree_skirt + pr_tree_garland + pr_tree_lights)


    # print(f"day : {days} n_ornament_set : {n_ornament_set} q_of_decorations : {q_decoration} total_spirit : {total_spirit}")
    # if days > 1 and (days - 1) % 2 == 0 and (days - 1) % 5 == 0:
    #     q_decoration += 2

    # print(f"days + {days} + total_spirit + {total_spirit} ")
if days_to_Christmas % 10 == 0:
    total_spirit -= 30
print(f"Total cost: {total_cost}")
print(f"Total spirit: {total_spirit}")

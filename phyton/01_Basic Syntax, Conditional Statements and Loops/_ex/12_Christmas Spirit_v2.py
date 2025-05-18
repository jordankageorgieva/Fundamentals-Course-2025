q_of_decorations = int(input())
days_to_Chr= int(input())

n_ornament_set = 0
n_tree_skirts = 0
n_tree_garlands = 0
n_tree_lights = 0
spirit = 0

if days_to_Chr < 10:
    middle_days = days_to_Chr
    for days in range(1, middle_days + 1):
        if days % 2 == 0:
            n_ornament_set += 1 * q_of_decorations
            print(f"day : {days} n_ornament_set : {n_ornament_set}")
        if days % 3 == 0:
            n_tree_skirts += 1 * q_of_decorations
            n_tree_garlands += 1 * q_of_decorations
        if days % 5 == 0:
            n_tree_lights += 1 * q_of_decorations
            if days % 3 == 0:
                spirit += 30
else:
    middle_days = 10

    for days in range(1, days_to_Chr + 1):
        if days % 11 == 0:
            q_of_decorations += 2
        if days % 2 == 0:
            n_ornament_set += 1 * q_of_decorations
        if days % 3 == 0:
            n_tree_skirts += 1 * q_of_decorations
            n_tree_garlands += 1 * q_of_decorations
        if days % 5 == 0:
            n_tree_lights += 1 * q_of_decorations
            if days % 3 == 0:
                spirit += 30

        if days % 10 == 0:
            spirit -= 20
        print(f"day : {days} n_ornament_set : {n_ornament_set} q_of_decorations : {q_of_decorations} spirit : {spirit}")

print(f"spirit1 : {spirit}")
if days_to_Chr % 10 == 0 :
    spirit -= 30
print(f"spirit2 : {spirit}")
# Totals
print(f"n_ornament_set : {n_ornament_set}")
print(f"n_tree_skirts : {n_tree_skirts}")
print(f"n_tree_garlands : {n_tree_garlands}")
print(f"n_tree_lights : {n_tree_lights}")
print(f"spirit : {spirit}")
total_cost = n_ornament_set * 2 + n_tree_skirts * 5 + n_tree_garlands * 3 + n_tree_lights * 15
total_spirit = spirit + n_ornament_set * 5 + n_tree_skirts * 3 + n_tree_garlands * 10 + n_tree_lights * 17

print(f"Total cost: {total_cost}")
print(f"Total spirit: {total_spirit}")
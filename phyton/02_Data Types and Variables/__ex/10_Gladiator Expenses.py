lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

expenses = 0
count_shield = 0
for index in range(1, lost_fights_count+ 1):
    if index % 2 == 0:
        expenses += helmet_price
        # print(f"expenses helmet = {expenses}")
    if index % 3 == 0:
        expenses += sword_price
        # print(f"expenses sword = {expenses}")
    if index % 2 == 0 and index % 3 == 0 :
        expenses += shield_price
        # print(f"expenses shield = {expenses}")
        count_shield += 1
        if count_shield % 2 == 0:
            expenses += armor_price
            count_shield = 0

print(f"Gladiator expenses: {expenses:.2f} aureus")
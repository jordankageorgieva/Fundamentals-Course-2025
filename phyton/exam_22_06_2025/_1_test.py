import math

# Input
budget = float(input())
students = int(input())
flour_price = float(input())
egg_price = float(input())
apron_price = float(input())

# Calculations
# 1. Aprons (20% more, rounded up)
aprons_needed = math.ceil(students * 1.2)
total_aprons_cost = aprons_needed * apron_price

# 2. Eggs (10 per student)
total_eggs_cost = students * 10 * egg_price

# 3. Flour (every 5th is free)
free_flour_packs = students // 5
flour_packs_needed = students - free_flour_packs
total_flour_cost = flour_packs_needed * flour_price

# Total cost
total_cost = total_aprons_cost + total_eggs_cost + total_flour_cost

# Output
if total_cost <= budget:
    print(f"Items purchased for {total_cost:.2f}$.")
else:
    needed_money = total_cost - budget
    print(f"{needed_money:.2f}$ more needed.")

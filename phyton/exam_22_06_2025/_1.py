import math
budget = float(input())
students = int(input())
pr_flour = float(input())
pr_egg = float(input())
pr_apron = float(input())

free_flour = students // 5
all_flour = students - free_flour
total_budget = pr_flour * all_flour + 10 * pr_egg * students + pr_apron * math.ceil(students * 1.2)
# print(total_budget)

if total_budget <= budget:
    print(f"Items purchased for {total_budget:.2f}$.")
else:
    need_m = total_budget - budget
    print(f"{need_m:.2f}$ more needed.")

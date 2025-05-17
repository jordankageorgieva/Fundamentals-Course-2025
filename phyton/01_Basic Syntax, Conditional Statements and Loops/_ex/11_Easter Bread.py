budget = float(input())
pr_flour = float(input())

pr_eggs = pr_flour * 0.75
pr_milk = pr_flour * 1.25

pr_bread = pr_flour + pr_eggs + (pr_milk * 0.25)

count = 0
eggs = 0
while budget > pr_bread:
    budget -= pr_bread
    count += 1
    eggs += 3
    if count % 3 == 0:
        eggs -= count -2
    # print(budget )

print(f"You made {count} loaves of Easter bread! Now you have {eggs} eggs and {budget:.2f}BGN left.")

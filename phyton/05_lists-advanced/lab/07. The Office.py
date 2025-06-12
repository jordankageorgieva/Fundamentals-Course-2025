employees_happiness = list(map(int, input().split(' ')))
factor = int(input())

everage = sum(employees_happiness)/len(employees_happiness)
more_happy = [emp for emp in employees_happiness if emp >= everage]
if len(more_happy) >= int(len(employees_happiness) / 2):
     print(f"Score: {len(more_happy)}/{len(employees_happiness)}. Employees are happy!")
else:
    print(f"Score: {len(more_happy)}/{len(employees_happiness)}. Employees are not happy!")

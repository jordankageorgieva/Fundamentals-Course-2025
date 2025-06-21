employee_efficiency_1_per_hour = int(input())
employee_efficiency_2_per_hour = int(input())
employee_efficiency_3_per_hour = int(input())
students_count = int(input())

sum_efficiency_per_hour = employee_efficiency_1_per_hour + employee_efficiency_2_per_hour + employee_efficiency_3_per_hour

hours = 0
delta = 0
while students_count > 0:
    # print(students_count)
    hours += 1
    if hours % 4 == 0:
        continue
    students_count -= sum_efficiency_per_hour

print(f"Time needed: {hours}h.")

numbers_of_people = int(input())
elevetor_capacity = int(input())

if numbers_of_people % elevetor_capacity == 0:
    print(numbers_of_people // elevetor_capacity)
else:
    print(numbers_of_people // elevetor_capacity + 1)
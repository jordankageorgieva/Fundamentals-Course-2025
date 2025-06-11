def is_perfect_number(number: int) -> bool:
    is_perfect = False
    sum_numbers = 0
    upper_limit = int(number / 2) + 1  # we make the half of the iterations to find out the perfect number
    # print(upper_limit)
    delta = 1
    for index in range(1, upper_limit, delta):
        if number % index == 0:
            sum_numbers += index
        delta += index
        if delta > upper_limit:
            break

    if sum_numbers == number:  # perfect number is a number where sum of all devisors are equal to the number
        # ex divisors of 6 are : 1, 2, 3 and sum = 1 + 2 + 3 == 6
        is_perfect = True

    return is_perfect


# number_to_test = int(input())
# for number_to_test in range(1, 100_000, 100):
while delta
    print(f"number! : {number_to_test} ")
    if is_perfect_number(number_to_test):
        print(f"We have a perfect number! : {number_to_test} ")
# if is_perfect_number(number_to_test):
#     print("We have a perfect number!")
# else:
#     print("It's not so perfect.")

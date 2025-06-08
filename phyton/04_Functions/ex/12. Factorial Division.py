def get_factorial(number: int) -> int:
    # print(f"incoming number is : {number}")
    # facturiel = number
    if number == 1:
        return number * 1

    return number * get_factorial(number -1)

number_1 = int(input())
number_2 = int(input())
factorial_division_1 = get_factorial(number_1)
factorial_division_2 = get_factorial(number_2)
factorial_division = factorial_division_1  /  factorial_division_2
print(f"{factorial_division:.02f}")
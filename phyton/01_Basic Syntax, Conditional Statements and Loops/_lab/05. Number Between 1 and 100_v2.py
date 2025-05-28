
is_ok_number = False
while not is_ok_number:
    number = float(input())
    if number >= 1 and number <= 100 :
        is_ok_number = True


if is_ok_number:
    print(f"The number {number} is between 1 and 100")
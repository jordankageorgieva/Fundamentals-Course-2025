number_of_strings = int(input())


for _ in range(number_of_strings):
    strings = input()

    is_pure = True
    for i in strings:
        if i == ',' or i == '.' or i == '_':
            print(f"{strings} is not pure!")
            is_pure = False
            break

    if is_pure:
        print(f"{strings} is pure.")


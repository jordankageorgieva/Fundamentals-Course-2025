def perfect_number(number: int, call_count: int) -> int:
    call_count += 1
    print(f"call_count {call_count}")
    print(number)
    print(f" to sum : {round(number/2)}")
    # if number % recurcion_number != 0:
    #     return number

    if number == 0 or number == 1:
        return 1

    return int((number-1)/2) + perfect_number(int((number-1)/4), call_count)



number = 28 #1236498
sum = perfect_number(number, 0)
print(sum)
# for number in range(1, 1_000):
#     if (perfect_number(number) == number):
#         print(f"perfect: {number}")
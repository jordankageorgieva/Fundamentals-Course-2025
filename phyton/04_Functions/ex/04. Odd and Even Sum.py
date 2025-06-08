def odd_and_even_sum(number: str) -> str:
    num_list = [int(d) for d in number]

    sum_even = 0
    sum_not_even = 0
    for index in range(0, len(num_list)):
        if num_list[index] % 2 == 0:
            sum_even += num_list[index]
        else:
            sum_not_even += num_list[index]

    return f"Odd sum = {sum_not_even}, Even sum = {sum_even}"


number = input()
print(odd_and_even_sum(number))

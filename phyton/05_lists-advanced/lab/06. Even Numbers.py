numbers = [int(num) for num in input().split(",")]
# even_numbers = [numbers.index(num) for num in numbers if num % 2 == 0]
even_numbers = [index for index in range(len(numbers)) if numbers[index] % 2 == 0]
print(even_numbers)
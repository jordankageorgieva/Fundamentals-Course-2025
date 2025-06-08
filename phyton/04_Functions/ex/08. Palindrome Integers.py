def is_palindrome(number: str) -> bool:
    is_palindrome = False
    reversed_number = number[::-1]
    if number == reversed_number:
        is_palindrome = True
    return is_palindrome
    # return number == number[::-1]

list_numbers = input().split(", ")
# list_numbers_to_int = [int(n) for n in list_numbers]
for number in list_numbers:
    print(is_palindrome(number))
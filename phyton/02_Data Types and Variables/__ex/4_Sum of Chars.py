num_lines = int(input())

sum_of_char = 0
for _ in range (num_lines):
    char = input()
    sum_of_char += ord(char)

print(f"The sum equals: {sum_of_char}")
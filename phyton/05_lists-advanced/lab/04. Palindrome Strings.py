words_sequence = input().split(' ')
palindrome = input()

palindrome_list = []
count_palindrome = 0
for word in words_sequence:
    if word == word[::-1]:
        palindrome_list.append(word)
    if word == palindrome:
        count_palindrome += 1

print(palindrome_list)
print(f"Found palindrome {count_palindrome} times")
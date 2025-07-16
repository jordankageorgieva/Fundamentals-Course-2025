def letter_position(letter):
    letter = letter.lower()
    return ord(letter) - ord('a') + 1

first_letter = "s"
second_letter = 'G'
number = 17
sum = 0
if first_letter.islower():
    sum += number * letter_position(first_letter)
elif first_letter.isupper():
    sum += number / letter_position(first_letter)
if second_letter.islower():
    sum += letter_position(second_letter)
elif second_letter.isupper():
    sum -= letter_position(second_letter)


print(sum)
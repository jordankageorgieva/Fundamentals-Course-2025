def letter_position(letter):
    letter = letter.lower()
    return ord(letter) - ord('a') + 1

letter_s = input().split(" ")
sum_total = 0
for letter in letter_s:
    if letter == '':
        continue
    # number = ""
    # letters = ''
    sum = 0
    # for i in range(len(letter)):
    #     if letter[i].isalpha():
    #         letters += letter[i]
    #     elif letter[i].isdigit():
    #         number += letter[i]
    # number = int(number.strip())

    first_letter = letter[0]
    second_letter = letter[-1]
    number = int(letter[1:len(letter) - 1])

    if first_letter.islower():
        sum += number * letter_position(first_letter)
    elif first_letter.isupper():
        sum += number / letter_position(first_letter)


    if second_letter.islower():
        sum += letter_position(second_letter)
    elif second_letter.isupper():
        sum -= letter_position(second_letter)


    sum_total += sum

print(f"{sum_total:.2f}")
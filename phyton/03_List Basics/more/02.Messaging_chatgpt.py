sequence_of_numbers = input()
list_seq_of_numbers = sequence_of_numbers.split(" ")

extract_letters_from_this_text = input()
extract_letters_list = list(extract_letters_from_this_text)

message = []

for num in list_seq_of_numbers:
    digit_sum = sum(int(d) for d in num)
    print(digit_sum)
    print(len(extract_letters_list))
    index = digit_sum % len(extract_letters_list)  # безопасен индекс
    print(index)
    letter = extract_letters_list.pop(index)
    message.append(letter)

print("".join(message))
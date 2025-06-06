sequence_of_numbers = input()
list_seq_of_numbers = sequence_of_numbers.split(" ")
# print(list_seq_of_numbers_to_int)

extract_letters_from_this_text = input()
extract_letters_from_this_text_list = [char for char in extract_letters_from_this_text]
message = []
for index in range(len(list_seq_of_numbers)):
    # print(list_seq_of_numbers_to_int[index])
    digit_sum = sum(int(d) for d in list_seq_of_numbers[index])
    # find  out the corresponding letter in the extract_letters_from_this_text
    letter = ''
    is_letter_found = False
    while not is_letter_found:

        if 0 <= digit_sum < len(extract_letters_from_this_text):
            #     get the letter
            letter = extract_letters_from_this_text_list[digit_sum]
            # add to the message and remove it from the string
            message.append(letter)
            extract_letters_from_this_text_list.remove(letter)
            is_letter_found = True
        elif digit_sum >= len(extract_letters_from_this_text):
            #  it need to be and equals
            #     make iteration of the next
            digit_sum -= len(extract_letters_from_this_text)
            continue
    # print(f"letter found {letter}")


print("".join(message))

_1_char_index = int(input())
_2_char_index = int(input())

ascii_table = ""
for i in range(_1_char_index, _2_char_index + 1):
    # print(i)
    # print(chr(i))
    ascii_table += chr(i)

print(" ".join(ascii_table))


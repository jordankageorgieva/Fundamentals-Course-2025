input_txt = input()

digit_lst = []

non_digit_lst = []
for index in range(len(input_txt)):
    if input_txt[index].isdigit():
        digit_lst.append(input_txt[index])
    else:
        non_digit_lst.append(input_txt[index])

# diversification
take_lst = []
skip_lst = []
for index in range(len(digit_lst)):
    if index % 2 == 0:
        take_lst.append(digit_lst[index])
    else:
        skip_lst.append(digit_lst[index])

# print(take_lst)
# print(skip_lst)

# data manipulation
result = []
# print(len(non_digit_lst))
step = 0
for index in range(len(take_lst)):
    _1_indx = int(take_lst[index])
    _2_indx = int(skip_lst[index])
    taken = non_digit_lst[0: _1_indx]

    inner_step = _1_indx + _2_indx
    step += _1_indx + _2_indx

    non_digit_lst = non_digit_lst[inner_step:]
    result.append(taken)

# final result
end_rope = ''
for item in result:
    if item != []:
        string = [str(i) for i in item]
        end_rope += "".join(string)

print(end_rope)

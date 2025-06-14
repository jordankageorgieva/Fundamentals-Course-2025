input_sequence_1 = input().split(", ")
input_sequence_2 = input().split(", ")

out_str = []
for str_1 in input_sequence_1:
    for str_2 in input_sequence_2:
        if str_1 in str_2 and str_1 not in out_str:
            out_str.append(str_1)
            # break


print(out_str)

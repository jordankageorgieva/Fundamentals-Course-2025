sequence_strings = input().split(" ")
for seq in sequence_strings:
    repeat_time = len(seq)
    print(repeat_time * seq, end="")
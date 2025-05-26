n = int(input())

for i in range (1, n + 1):
    sum = 0
    i_to_str = str(i)
    # print(i_to_str)
    for j in range(len(i_to_str)):
       sum += int(i_to_str[j])

    if sum == 5 or sum == 7 or sum == 11:
        print(f"{i} -> True")
    else:
        print(f"{i} -> False")
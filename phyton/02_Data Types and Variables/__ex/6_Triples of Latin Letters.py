n = int(input())

for i_1 in range(0, n):
    for i_2 in range(0, n):
        for i_3 in range(0, n):
            print(f"{chr(97+i_1)}{chr(97+i_2)}{chr(97+i_3)}")

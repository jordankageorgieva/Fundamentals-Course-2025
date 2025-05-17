n = int(input())

for i in range(n):
    read_num = int(input())
    if read_num % 2 != 0:
        print(f"{read_num} is odd!")
        break
else:
    print("All numbers are even.")
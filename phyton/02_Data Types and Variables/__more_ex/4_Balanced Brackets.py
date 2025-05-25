lines_number = int(input())

balance = 0
for index in range(lines_number):
    row = input()
    # print(row)
    if "(" in row:
        balance += 1
    elif ")" in row:
        balance -= 1
    # print(f" balance = {balance}")

if balance == 0:
    print("BALANCED")
else:
    print("UNBALANCED")
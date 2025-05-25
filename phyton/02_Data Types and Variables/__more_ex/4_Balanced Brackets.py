lines_number = int(input())

spin = 0
marked_as_unbalanced = False
for index in range(lines_number):
    row = input()
    # print(row)
    if "(" == row:
        spin += 1
        if spin > 1:
            marked_as_unbalanced = True
    elif ")" == row:
        spin -= 1
        if spin < 0:
            marked_as_unbalanced = True
    elif (row.isascii() or row.isdigit()) and "(" not in row and ")" not in row:
        continue
    # print(f" balance = {balance}")

if spin == 0 and marked_as_unbalanced == False:
    print("BALANCED")
else:
    print("UNBALANCED")

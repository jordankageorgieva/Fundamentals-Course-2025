divisor = int(input())
boundary = int(input())

number = 0
if boundary % divisor == 0:
    number = boundary
else:
    for index in range (boundary, divisor -1, -1):
        if index % divisor == 0:
            number = index
            break

print(number)
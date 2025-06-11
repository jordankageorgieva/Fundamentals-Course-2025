
depth_tribonaci = int(input())

def tribanaci_sequence(depth: int):
    if depth <= 0:
        return

    first = 1
    if depth >= 1:
        print(f"{first}", end = ' ')
    second = 1
    if depth >= 2:
        print(f"{second}", end = ' ')
    third = 2
    if depth >= 3:
        print(f"{third}" , end = ' ')

    for index in range(3, depth):
        sum = first + second + third
        if index == depth:
            print(f"{sum}")
        else:
            print(f"{sum}", end=' ')
        first = second
        second = third
        third = sum

tribanaci_sequence(depth_tribonaci)
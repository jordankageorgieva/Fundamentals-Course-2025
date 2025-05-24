import math

gr_size = int(input())
days = int(input())

sum = 0
for day in range(1, days + 1):
    if day % 10 == 0:
        gr_size -= 2
    if day % 15 == 0:
        gr_size += 5

    sum += 50
    # food
    sum -= gr_size * 2
    if day % 3 == 0:
        sum -= gr_size * 3

    if day % 5 == 0:
        sum += gr_size * 20
        if day % 3 == 0:
            sum -= gr_size * 2



print(f"{gr_size} companions received {math.floor(sum/gr_size)} coins each.")
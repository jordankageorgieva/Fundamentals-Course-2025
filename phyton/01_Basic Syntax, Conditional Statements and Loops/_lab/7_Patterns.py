num = int(input())

i = 1
while i <= num:
    j = 1
    while j <= i:
        print("*",end="")
        j += 1
    print()
    i += 1

k = num - 1
while k >= 1:
    j = 1
    while j <= k:
        print("*",end="")
        j += 1
    print()
    k -= 1

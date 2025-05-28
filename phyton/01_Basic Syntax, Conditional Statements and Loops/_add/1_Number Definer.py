float_n = float(input())
if float_n == 0 :
    print("zero")
elif float_n > 0 :
    if 0 < float_n < 1:
        print("small positive")
    else:
        print("positive")
elif float_n < 0 :
    if 0 < abs(float_n) < 1:
        print("small negative")
    else:
        print("negative")


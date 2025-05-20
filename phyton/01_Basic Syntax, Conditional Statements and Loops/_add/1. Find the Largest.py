number = int(input())
#  find the bigest n
digits = sorted(str(number), reverse=True)
max = int(''.join(digits))
print(max)
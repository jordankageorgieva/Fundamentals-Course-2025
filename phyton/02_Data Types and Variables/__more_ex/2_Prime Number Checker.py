prime = int(input())

is_prime = True
for index in range (prime -1, 1, -1):
    if prime % index == 0:
        is_prime = False
        break

if is_prime :
    # print(f"the {prime} is prime number")
    print(f"True")
else:
    # print(f"the {prime} is NOT prime number")
    print("False")
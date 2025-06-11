
def multiplication_sign (a: int, b: int, c: int) -> str:
    if a == 0 or b == 0 or c == 0:
        return "zero"

    sign_negative_count = 0
    if a < 0:
        sign_negative_count += 1

    if b < 0:
        sign_negative_count += 1

    if c < 0:
        sign_negative_count += 1

    if sign_negative_count % 2 == 0:
        return "positive"
    else:
        return "negative"

a = int(input())
b = int(input())
c = int(input())

print(multiplication_sign(a, b, c))
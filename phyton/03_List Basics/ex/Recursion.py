def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

def sum(n):
    print(n)
    if n == 0:
        return 1
    return n + sum(n + 1)

print(sum(10))
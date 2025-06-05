def calculate(operation: str, param_1: int, param_2: int):
    result = None
    if 'multiply' == operation:
        result = param_1 * param_2
    elif 'divide' == operation:
        result = int(param_1 / param_2)
    elif 'add' == operation:
        result = param_1 + param_2
    elif 'subtract' == operation:
        result = param_1 - param_2
    return result


operation = input()
param_1 = int(input())
param_2 = int(input())

print(calculate(operation, param_1, param_2))

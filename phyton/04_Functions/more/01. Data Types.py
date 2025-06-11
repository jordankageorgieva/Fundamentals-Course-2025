type_value = input()
value_type = input()


def convert_type_value_to_value_type(type_value: str, value_type: str) -> str:
    if type_value == 'string':
        return '$' + value_type + '$'
    elif type_value == 'int':
        return 2 * int(value_type)
    elif type_value == 'real':
        return f"{1.5 * float(value_type):.02f}"


print(convert_type_value_to_value_type(type_value, value_type))

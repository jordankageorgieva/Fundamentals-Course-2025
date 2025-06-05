def get_absolute_values(data: str):
    data_list = data.split(' ')
    absolute_values = [abs(float(data)) for data in data_list]
    return absolute_values


sequence = input()

print(get_absolute_values(sequence))

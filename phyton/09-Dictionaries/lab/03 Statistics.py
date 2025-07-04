
input_data = input()

product_dict = dict()
while input_data != 'statistics':

    key, value = input_data.split(":")
    value = int(value)
    if key in product_dict:
        product_dict[key] += value
    else:
        product_dict[key] = value

    input_data = input()

count_all_products = len(product_dict.items())
sum_all_quantities = sum([product_dict.get(item) for item in product_dict])

print("Products in stock:")
for item in product_dict:
    print(f"- {item}: {product_dict.get(item)}")
print(f"Total Products: {count_all_products}")
print(f"Total Quantity: {sum_all_quantities}")

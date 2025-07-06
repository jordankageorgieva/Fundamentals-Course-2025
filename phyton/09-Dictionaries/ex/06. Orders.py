product_line = input()
product = {}
while product_line != 'buy':
    name, price, quantity = product_line.split(" ")
    price = float(price)
    quantity = int(quantity)
    if name in product.keys():
        current_price, current_quantity = product[name]
        current_quantity = int(current_quantity)

        current_quantity += quantity
        product[name] = [price, current_quantity]
    else:
        product[name] = [price, quantity]

    product_line = input()

# print(product)
print("\n".join([key + f" -> {price * quantity:.02f}" for key, [price, quantity] in product.items()]))
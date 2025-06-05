def calculate_orders(product: str, quantity: int):
    total_price = None
    if  "coffee" == product:
        total_price = 1.5 * quantity
    elif "water" == product:
        total_price = 1 * quantity
    elif "coke" == product:
        total_price = 1.40 * quantity
    elif "snacks" == product:
        total_price = 2.0 * quantity

    return f"{total_price:.2f}"

product = input()
quantity = int(input())

print(calculate_orders(product, quantity))
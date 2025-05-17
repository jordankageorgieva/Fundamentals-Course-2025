num_orders = int(input())

total_price = 0
for index in range(num_orders):

    price_capsule = float(input())
    days = int(input())
    capsules_need_per_day = int(input())

    # data checks
    if price_capsule < 0.01 or price_capsule > 100.00:
        continue
    elif days < 1 or days > 31:
        continue
    elif capsules_need_per_day < 1 or capsules_need_per_day > 2_000:
        continue

    price_coffe = price_capsule * capsules_need_per_day * days
    print(f"The price for the coffee is: ${price_coffe:.2f}")
    total_price += price_coffe


print(f"Total: ${total_price:.2f}")
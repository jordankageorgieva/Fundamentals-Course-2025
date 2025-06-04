ticket_price_to_the_moon = 150
input_items_to_sell = input()
budget = int(input())
# data parse
items_to_sell = input_items_to_sell.split('|')

item_to_buy = []
profit = 0
index = 0
while index < len(items_to_sell):

    # outbox
    item_type, item_price = items_to_sell[index].split("->")
    item_price = float(item_price)
    index += 1
    # print(f"{item_type}, {item_price}")

    if item_type == 'Clothes' and item_price <= 50:
        if budget - item_price < 0:
            continue

        budget -= item_price
        new_price = item_price * 1.4
        profit += new_price - item_price
        item_to_buy.append(new_price)
    elif item_type == 'Shoes' and item_price <= 35:
        if budget - item_price < 0:
            continue

        budget -= item_price
        new_price = item_price * 1.4
        profit += new_price - item_price
        item_to_buy.append(new_price)
    elif item_type == 'Accessories' and item_price <= 20.50:
        if budget - item_price < 0:
            continue

        budget -= item_price
        new_price = item_price * 1.4
        profit += new_price - item_price
        item_to_buy.append(new_price)

# out data

result = " ".join(f"{item:.2f}" for item in item_to_buy)
print(result)

print(f"Profit: {profit:.2f}")

new_calculated_budget = budget + sum(item_to_buy)
if new_calculated_budget > ticket_price_to_the_moon:
    print(f"Hello, France!")
else:
    print(f"Not enough money.")

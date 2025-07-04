elements = [element for element in input().split(" ")]
search_elements = [element for element in input().split(" ")]

stocks = {}

for index in range(0, len(elements), 2):
    key = elements[index]
    value = int(elements[index + 1])
    stocks[key] = value

for element in search_elements:
    if stocks.get(element) != None:
        quantity = stocks.get(element)
        print(f"We have {quantity} of {element} left")
    else:
        print(f"Sorry, we don't have {element}")
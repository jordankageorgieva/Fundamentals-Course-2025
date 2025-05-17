age = int(input())

drink_name = ""
if age <= 14:
    drink_name = "toddy"
elif age <= 18:
    drink_name = "coke"
elif age <= 21:
    drink_name = "beer"
else:
    drink_name = "whisky"

print(f"drink {drink_name}")

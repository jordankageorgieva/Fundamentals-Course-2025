numbers_of_lines = int(input())

tank_capacity = 255
sum_liquidity = 0

for index in range (numbers_of_lines):
    currenet_liquidity = int(input())
    sum_liquidity += currenet_liquidity
    if tank_capacity - sum_liquidity < 0:
        sum_liquidity -= currenet_liquidity
        print(f"Insufficient capacity!")

print(f"{sum_liquidity}")
number_of_snowballs = int(input())

highest_snowball_value = 0
snowball_weight = 0
snowball_time = 0
snowball_quality = 0
for index in range(number_of_snowballs):
    weight_snowball = int(input())
    time_snowball = int(input())
    quality_snowball = int(input())

    snowball_value = (weight_snowball / time_snowball) ** quality_snowball
    if snowball_value > highest_snowball_value:
        highest_snowball_value = snowball_value
        snowball_weight = weight_snowball
        snowball_time = time_snowball
        snowball_quality = quality_snowball


print(f"{snowball_weight} : {snowball_time} = {int(highest_snowball_value)} ({snowball_quality})")


for index in range (1, 10):
    print( f" index  to the {index} power {index ** index}")


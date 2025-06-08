seq_numbers_in = input().split(" ")
seq_numbers = [int(num) for num in seq_numbers_in]

index = (len(seq_numbers)) // 2
speed_car_1 = seq_numbers[:index]
speed_car_2 = seq_numbers[-1:index:-1]  # reversed second half

sum_speed_car_1 = 0
for speed in speed_car_1:
    if speed == 0:
        sum_speed_car_1 *= 0.8
    else:
        sum_speed_car_1 += speed

sum_speed_car_2 = 0
for speed in speed_car_2:
    if speed == 0:
        sum_speed_car_2 *= 0.8
    else:
        sum_speed_car_2 += speed

if sum_speed_car_1 < sum_speed_car_2 :
    print(f"The winner is left with total time: {sum_speed_car_1:.1f}")
else:
    print(f"The winner is right with total time: {sum_speed_car_2:.1f}")
room_numbers = int(input())

free_chairs = 0
index = 1
game_on = True
while index <= room_numbers:
    chairs, visitors_number = input().split(" ")
    numbers_chairs = [ chair for chair in chairs ]
    # print(numbers_chairs)
    if int(visitors_number) > len(numbers_chairs):
        n_chairs = int(visitors_number) - len(numbers_chairs)
        print(f"{n_chairs} more chairs needed in room {index}")
        game_on = False
    free_chairs += (len(numbers_chairs) - int(visitors_number))
    index += 1

if game_on:
    print(f"Game On, {free_chairs} free chairs left")
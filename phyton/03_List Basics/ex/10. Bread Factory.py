initial_energy = 100
initial_coins = 100

working_day_event_input = input()
# parse data
working_day_event = working_day_event_input.split("|")
# print(working_day_event)

index = 0
gain_energy = initial_energy
is_closed = False
while index < len(working_day_event):
    # outbox
    event_type, number = working_day_event[index].split("-")
    number = int(number)
    index += 1

    # print(f"{event_type} - {number}")

    if event_type == 'rest':
        # previous_energy = gain_energy
        # gain_energy = min(gain_energy + number, initial_energy)
        # gained = gain_energy - previous_energy
        # print(f"You gained {gained} energy.")
        # print(f"Current energy: {gain_energy}.")
        if gain_energy + number >= initial_energy:
            print(f"You gained {gain_energy - initial_energy} energy.")
            print(f"Current energy: {gain_energy}.")
        else:
            gain_energy += number
            print(f"You gained {number} energy.")
            print(f"Current energy: {gain_energy}.")
    elif event_type == 'order':
        if gain_energy - 30 >= 0:
            initial_coins += number
            gain_energy -= 30
            print(f"You earned {number} coins.")
        else:
            gain_energy += 50
            print("You had to rest!")

        # print(f"initial_coins: {initial_coins}.")
        # print(f"initial_energy: {gain_energy}.")
    else:
        if initial_coins - number >= 0:
            initial_coins -= number
            print(f"You bought {event_type}.")
        else:
            is_closed = True
            print(f"Closed! Cannot afford {event_type}.")
            break

            # print(f"initial_coins: {initial_coins}.")
            # print(f"initial_energy: {gain_energy}.")

if not is_closed:
    print("Day completed!")
    print(f"Coins: {initial_coins}")
    print(f"Energy: {gain_energy}")
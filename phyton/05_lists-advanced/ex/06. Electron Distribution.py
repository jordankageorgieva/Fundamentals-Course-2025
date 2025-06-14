electrons_number = int(input())
shells_number = 1

electrons_on_shells = []
sum_electrons = 0
while sum_electrons < electrons_number:
    number_electrons = 2 * (shells_number ** 2)
    if number_electrons + sum_electrons > electrons_number:
        electrons_on_shells.append(electrons_number - sum_electrons)
    else:
        electrons_on_shells.append(number_electrons)
    sum_electrons += number_electrons
    shells_number += 1

print(electrons_on_shells)
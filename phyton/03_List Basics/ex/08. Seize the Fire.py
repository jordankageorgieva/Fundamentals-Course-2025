fire_level = input()
water_amount= int(input())
# data parse
fire_cells = fire_level.split('#')

burn_out_fire_cells = []
effort_to_butn_out_the_fire = 0
tatal_burn_out_cells = 0
index = 0
while index < len(fire_cells):
    # print(fire_cells[index])
    # outbox
    fire_type, value = fire_cells[index].split(" = ")
    value = int(value)
    index += 1

    if fire_type == 'High' and 81 <= value <= 125:
        if water_amount-value <0:
            continue

        burn_out_fire_cells.append(value)
        # reduce water
        water_amount -= value
        # effort calculate
        effort_to_butn_out_the_fire += 0.25 * value
        # burn out
        tatal_burn_out_cells += value
    elif fire_type == 'Medium' and 51 <= value <= 80:
        if water_amount - value < 0:
            continue
        burn_out_fire_cells.append(value)
        # reduce water
        water_amount -= value
        # effort calculate
        effort_to_butn_out_the_fire += 0.25 * value
        # burn out
        tatal_burn_out_cells += value
    elif fire_type == 'Low' and 1 <= value <= 50:
        if water_amount - value < 0:
            continue
        burn_out_fire_cells.append(value)
        # reduce water
        water_amount -= value
        # effort calculate
        effort_to_butn_out_the_fire += 0.25 * value
        # burn out
        tatal_burn_out_cells += value



# print(f"Cells: {seize_fire_cells}")
print("Cells:")
for cell in burn_out_fire_cells:
    print(f" - {cell}")
print(f"Effort: {effort_to_butn_out_the_fire:.2f}")
print(f"Total Fire: {tatal_burn_out_cells}")
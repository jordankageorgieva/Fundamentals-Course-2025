initial_energy = int(input())

battle_count = 0
while initial_energy > 0:
    enemy_distance = int(input())
    initial_energy -= enemy_distance
    if initial_energy 
    battle_count += 1

if initial_energy == 0 :
    print(f"Not enough energy! Game ends with {battle_count} won battles and {initial_energy} energy")
else:
    print(f"Won battles: {battle_count}. Energy left: {initial_energy}")
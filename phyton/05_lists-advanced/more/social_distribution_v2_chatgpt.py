population = list(map(int, input().split(", ")))
min_wealth = int(input())

total_wealth = sum(population)
required_wealth = len(population) * min_wealth

if total_wealth < required_wealth:
    print("No equal distribution possible")
else:
    n = len(population)

    # Step 1: Compute deficit for poor people
    deficit = 0
    for amount in population:
        if amount < min_wealth:
            deficit += min_wealth - amount

    # Step 2: Compute total surplus and collect surplus data
    surplus = 0
    surplus_indices = []
    for i in range(n):
        if population[i] > min_wealth:
            surplus_amount = population[i] - min_wealth
            surplus += surplus_amount
            surplus_indices.append((i, surplus_amount))

    # Step 3: Bring all poor people to min_wealth
    for i in range(n):
        if population[i] < min_wealth:
            population[i] = min_wealth

    # Step 4: Distribute deficit proportionally among the surplus people
    for i, person_surplus in surplus_indices:
        share = (person_surplus / surplus) * deficit
        population[i] -= share

    # Optional: Round values to integers if needed
    population = [round(p) for p in population]

    print(population)

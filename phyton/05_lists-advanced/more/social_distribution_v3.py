population = list(map(int, input().split(", ")))
min_wealth = int(input())

total_wealth = sum(population)
required_wealth = len(population) * min_wealth

if total_wealth < required_wealth:
    print("No equal distribution possible")
else:
    n = len(population)

    # Step 1: Calculate total deficit
    deficit = sum(min_wealth - p for p in population if p < min_wealth)

    # Step 2: Raise all poor people to min_wealth
    for i in range(n):
        if population[i] < min_wealth:
            population[i] = min_wealth

    # Step 3: Find contributors (those with wealth > min_wealth originally)
    # and calculate total wealth of contributors
    original = population  # original values (you must enter it again here)
    contributors = [(i, original[i]) for i in range(n) if original[i] > min_wealth]
    total_contrib_wealth = sum(w for _, w in contributors)

    # Step 4: Take proportional amount from each contributor based on original wealth
    for i, wealth in contributors:
        share = (wealth / total_contrib_wealth) * deficit
        population[i] = round(original[i] - share)

    print(population)

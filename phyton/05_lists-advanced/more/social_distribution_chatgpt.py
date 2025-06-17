population = list(map(int, input().split(", ")))
min_wealth = int(input())

total_wealth = sum(population)
required_wealth = len(population) * min_wealth

if total_wealth < required_wealth:
    print("No equal distribution possible")
else:
    # sort_population = sorted(population, reverse=True)
    # print(sort_population)
    for i in range(len(population)):
        if population[i] < min_wealth:
            # Find someone to give enough to reach min_wealth
            needed = min_wealth - population[i]

            for j in range(len(population) -1, 0, -1):
                if population[j] > min_wealth:
                    give = min(population[j] - min_wealth, needed)
                    population[j] -= give
                    population[i] += give
                    needed -= give
                if needed == 0:
                    break
    print(population)


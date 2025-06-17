population = list(map(int, input().split(", ")))
min_wealth = int(input())

min_sum_delta_in_system = 0
max_sum_delta_in_system = 0
for index in range(len(population)):
    if population[index] < min_wealth:
        min_sum_delta_in_system += min_wealth - population[index]
    else:
        max_sum_delta_in_system += population[index] - min_wealth

global_delta = max_sum_delta_in_system - min_sum_delta_in_system
if global_delta >= 0 :
    sum = 0
    new_population_delta = []
    for index in range(len(population)):
        if population[index] < min_wealth:
            delta = min_wealth - population[index]
            sum -= min_wealth - population[index]
            new_population_delta.append(delta)
        else:
            delta = population[index] - min_wealth
            sum += population[index] - min_wealth
            new_population_delta.append(delta)

    min_sum_in_system = 0
    max_value_index_in_system = max(population)
    for index in range(len(new_population_delta)):
        if new_population_delta[index] < min_wealth:
            min_sum_in_system += new_population_delta[index]
            population[index] = min_wealth

    # get money from max value
    max_index = population.index(max_value_index_in_system)
    if min_sum_in_system < max_value_index_in_system:
        max_value_index_in_system -= min_sum_in_system
        population[max_index] = max_value_index_in_system


    print(population)
else:
    print("No equal distribution possible")

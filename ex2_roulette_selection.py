import numpy as np

dimensions = 3
d = 3
A = np.asarray([[-2, 1, 0], [1, -2, 1], [0, 1, -2]])
b = np.asarray([-14, 14, -2])
c = -23.5
population_size = 50
crossover_prob = 0.9
mutation_prob = 0.05
iterations = 1000
# parents_number = int(0.3* population_size)
# parents_number = population_size

species_not_crossovered = []
species_to_crossover = []
crossovered_species = []

def function_f(A, b, c, cur_x):
    x = np.asarray(cur_x)
    a1 = np.dot(b.transpose(), x)
    a2 = np.dot(np.dot(x.transpose(), A), x)
    return c + a1 + a2

def fitness(A, b, c, current_x):
    fitness = function_f(A, b, c, current_x)
    return fitness

def roulette_selection(pop):
    fitness_vals = []
    population = np.asarray(pop)
    fit = []
    for chromosome in population:
        curr_fitness = fitness(A, b, c, chromosome)
        fit.append(curr_fitness)
        fitness_vals.append((curr_fitness, chromosome))

    max_fit = max(fit)
    min_fit = min(fit)
    roulette_wheel = []
    parents = []

    fit.sort()
    # fit.sort(reverse = True)
    # print("fit")
    # print(fit)
    # fitness_vals = sorted(fitness_vals, key=lambda x: x[0], reverse = True)
    fitness_vals = sorted(fitness_vals, key=lambda x: x[0])

    # Rescale range to [0, 1]
    fit_rescale = []
    sum = 0
    for f in fit:
        if (max_fit == min_fit):
            res_val = 1
        else:
            res_val = (f - min_fit) / (max_fit - min_fit)
        sum += res_val
        fit_rescale.append(res_val)

    wheel = []
    wheel.append(0)
    prev = 0
    if sum != 0:
        for fit_res in fit_rescale:
            wheel.append(prev + (fit_res / sum))
            prev = prev + (fit_res / sum)

    # print(wheel)
    # Spin roulette wheel.
    for i in range(population_size):
        spin = np.random.uniform(0.0, 1.0)
        # print("rand", spin)

        i = 0
        while i in range(len(wheel)) and wheel[i] < spin:
            i = i + 1

        if (i != 0):
            i = i - 1

        parent = fitness_vals[i][1]
        # print(fitness_vals[i][0], fitness_vals[i][1])
        parents.append(parent)
    # print(parents)
    return parents





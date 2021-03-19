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

parents_number = 25

species_not_crossovered = []
species_to_crossover = []
crossovered_species = []

def function_f(A, b, c, cur_x):
    x = np.asarray(cur_x)
    a1 = np.dot(b.transpose(), x)
    a2 = np.dot(np.dot(x.transpose(), A), x)
    return c + a1 + a2


current_x = np.random.uniform(low=-5.0, high=5.0, size=d)

def fitness(A, b, c, current_x):
    fitness = function_f(A, b, c, current_x)
    return fitness

def roulette_selection(pop):
    # define array with fitness values.
    fitness_vals = []
    population = np.asarray(pop)

    for chromosome in population:
        fitness_vals.append(((fitness(A, b, c, chromosome), chromosome)))

    roulette_wheel = []
    parents = []
    # Fill roulette_wheel with fitness values - each value is inserted into roulette_wheel array as many times as its value.
    for fit in range(len(fitness_vals)):
        r = fitness_vals[fit][0]
        for i in range(abs(int(r))):
            el = fitness_vals[fit]
            roulette_wheel.append(el[1])

    # Spin roulette wheel.
    for i in range(parents_number):
        index = np.random.randint(0, len(roulette_wheel))
        parent = roulette_wheel[index]
        parents.append(parent)   # Parent is a tuple of fitness and chromosome - we want to get only chromomes in parents array.

    return parents





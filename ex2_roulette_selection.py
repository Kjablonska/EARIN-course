import numpy as np

dimensions = 3
d = 3
A = np.asarray([[-2, 1, 0], [1, -2, 1], [0, 1, -2]])
b = np.asarray([-14, 14, -2])
c = -23.5
population_size = 50
crossover_prob = 0.9
mutation_prob = 0.05


def function_f(A, b, c, cur_x):
    x = np.asarray(cur_x)
    a1 = np.dot(b.transpose(), x)
    a2 = np.dot(np.dot(x.transpose(), A), x)
    return c + a1 + a2

def fitness(A, b, c, current_x):
    fitness = function_f(A, b, c, current_x)
    return fitness

def roulette_selection(pop):
    population = np.asarray(pop)
    fit = []
    for chromosome in population:
        fit.append(fitness(A, b, c, chromosome))

    max_fit = max(fit)
    min_fit = min(fit)
    roulette_wheel = []
    parents = []

    # Rescale range to [0, 1]
    fit_rescale = []
    sum = 0
    for f in range(len(fit)):
        if (max_fit == min_fit):
            res_val = 1
        else:
            res_val = (fit[f] - min_fit) / (max_fit - min_fit)
        sum += res_val
        fit_rescale.append((res_val, population[f]))

    wheel = []
    prev = 0
    if sum != 0:
        for fit_res in fit_rescale:
            curr = prev + (fit_res[0] / sum)
            wheel.append(curr)
            prev = curr

    # Select parents using roulette wheel.
    for _ in range(population_size):
        spin = np.random.uniform(0, 1)
        i = 0
        while i in range(len(wheel)) and wheel[i] < spin:
            i = i + 1

        parent = fit_rescale[i][1]
        parents.append(parent)

    return parents
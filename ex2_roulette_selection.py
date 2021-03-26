import numpy as np


def function_f(A, b, c, cur_x):
    x = np.asarray(cur_x)
    a1 = np.dot(b.transpose(), x)
    a2 = np.dot(np.dot(x.transpose(), A), x)
    return c + a1 + a2


def fitness(A, b, c, current_x):
    fitness_var = function_f(A, b, c, current_x)
    return fitness_var


def roulette_selection(pop, _matrix_a, _vector_b, _scalar_c, _population_size):
    population = np.asarray(pop)
    fit = []
    for chromosome in population:
        fit.append(fitness(_matrix_a, _vector_b, _scalar_c, chromosome))

    max_fit = max(fit)
    min_fit = min(fit)
    parents = []

    # Rescale range to [0, 1]
    fit_rescale = []
    sum = 0
    for f in range(len(fit)):
        if max_fit == min_fit:
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
    # There are selected as many parents as population size.
    for _ in range(_population_size):
        spin = np.random.uniform(0, 1)
        i = 0
        while i in range(len(wheel)) and wheel[i] < spin:
            i = i + 1

        parent = fit_rescale[i][1]
        parents.append(parent)

    return parents

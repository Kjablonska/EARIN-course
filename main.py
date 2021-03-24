import numpy as np
import ex2_roulette_selection as select
import ex2_crossover as crossover
import ex2_mutation as mutate


def run_method(_matrix_a, _vector_b, _scalar_c, _dimension, _population_size, _cross_probability, _mutation_probability):
    population = generate_population(_dimension, _vector_b, _population_size)
    for i in range(_population_size):
        parents = select.roulette_selection(population, _matrix_a, _vector_b, _scalar_c)
        crossovered = crossover.crossover(parents, _cross_probability)
        population = mutate.mutate(crossovered, _mutation_probability)
        print(population)
        print(function_f(_matrix_a, _vector_b, _scalar_c, population[np.random.randint(0, len(population))]))

    print("population")
    print(population)
    print(function_f(_matrix_a, _vector_b, _scalar_c, population[np.random.randint(0, len(population))]))


def generate_population(d, b, _population_size):
    population = []
    pow = np.power(2, d)
    for i in range(_population_size):
        x = np.random.randint(-pow, pow - 1, b.size)
        population.append(x)
    return population


def function_f(A, b, c, cur_x):
    x = np.asarray(cur_x)
    a1 = np.dot(b.transpose(), x)
    a2 = np.dot(np.dot(x.transpose(), A), x)
    return c + a1 + a2

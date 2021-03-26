import numpy as np
import ex2_roulette_selection as select
import ex2_crossover as crossover
import ex2_mutation as mutate
from scipy.stats import mode


def run_method(_matrix_a, _vector_b, _scalar_c, _int_d, _dimension, _population_size, _cross_probability, _mutation_probability, _no_iter):

    population = generate_population(_dimension, _int_d, _population_size)
    for i in range(_no_iter):
        parents = select.roulette_selection(population, _matrix_a, _vector_b, _scalar_c, _population_size)
        crossovered = crossover.crossover(parents, _cross_probability)
        population = mutate.mutate(crossovered, _mutation_probability, _int_d)

    print("Output population:")
    print(population)
    most_frequent = mode(population)
    sol = most_frequent.mode[0]
    print("Solution: ", sol)
    print("Function value: ", function_f(_matrix_a, _vector_b, _scalar_c, sol))


def generate_population(_dim, _int_d, _population_size):
    population = []
    pow = 2**(_int_d)
    for i in range(_population_size):
        x = np.random.randint(-pow, pow, _dim)
        population.append(x)
    return np.asarray(population)


def function_f(_matrix_a, _vector_b, _scalar_c, cur_x):
    x = np.asarray(cur_x)
    a1 = np.dot(_vector_b.transpose(), x)
    a2 = np.dot(np.dot(x.transpose(), _matrix_a), x)
    return _scalar_c + a1 + a2

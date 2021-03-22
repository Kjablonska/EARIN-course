import numpy as np
import ex2_roulette_selection as select
import ex2_crossover as crossover
import ex2_mutation as mutate

dimensions = 3
d = 3
A = np.asarray([[-2, 1, 0], [1, -2, 1], [0, 1, -2]])
b = np.asarray([-14, 14, -2])
c = -23.5
population_size = 50
crossover_prob = 0.9
mutation_prob = 0.05
iterations = 1000

def main():
    population = generate_population(d, b)
    for i in range(iterations):
        parents = select.roulette_selection(population)
        crossovered = crossover.crossover(parents)
        population = mutate.mutate(crossovered)

    print("population")
    print(population)
    print(function_f(A, b, c, population[1]))
    print("size", len(population))


def generate_population(d, b):
    population = []
    pow = np.power(2, d)
    for i in range(population_size):
        x = np.random.randint(-pow, pow - 1, b.size)
        population.append(x)
    return population


def function_f(A, b, c, cur_x):
    x = np.asarray(cur_x)
    a1 = np.dot(b.transpose(), x)
    a2 = np.dot(np.dot(x.transpose(), A), x)
    return c + a1 + a2

main()
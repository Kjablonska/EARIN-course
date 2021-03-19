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
        # print("population", i)
        # print(len(population))
        crossovered = crossover.crossover(parents)
        population = mutate.mutate(crossovered)


    print("population")
    print(population)


def generate_population(d, b):
    population = []
    pow = np.power(2, d)
    for i in range(population_size):
        x = np.random.randint(-pow, pow, b.size)

        # x = np.random.uniform(float(i - pow), float(pow), b.size)
        population.append(x)

    return population

main()
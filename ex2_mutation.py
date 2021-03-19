import numpy as np
from codecs import decode
import struct

dimensions = 3
d = 3
A = np.asarray([[-2, 1, 0], [1, -2, 1], [0, 1, -2]])
b = np.asarray([-14, 14, -2])
c = -23.5
population_size = 50
crossover_prob = 0.9
mutation_prob = 0.05
iterations = 1000

def choose_chromosomes_to_mutate(population):
    to_mutate = []
    not_to_mutate = []

    for chromosome in population:
        if np.random.uniform(0, 1) < mutation_prob:
            to_mutate.append(chromosome)
        else:
            not_to_mutate.append(chromosome)
    return to_mutate, not_to_mutate



def mutate(population):
    to_mutate, not_to_mutate = choose_chromosomes_to_mutate(population)

    for i in range(len(to_mutate)):
        index = np.random.randint(0, len(to_mutate[i]))
        vec_to_mutate = to_mutate[i]
        if vec_to_mutate[index] == 0:
            vec_to_mutate[index] = 1
        else:
            vec_to_mutate[index] = 0

    new_population_bin = to_mutate + not_to_mutate
    # print("new pop")
    # print(new_population_bin)
    new_population = []

    for i in range(len(new_population_bin)):
        # print(''.join([str(elem) for elem in new_population_bin[i]]))
        new_el = []
        for elem in new_population_bin[i]:
            str_bin = ''.join(str(elem))
            new_el.append(int(str_bin, 2))

        # str_bin = ''.join([str(elem) for elem in new_population_bin[i]])
        # new_population.append(bin_to_float(str_bin))
        new_population.append(new_el)

    return new_population


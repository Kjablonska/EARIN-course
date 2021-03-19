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
iterations = 100

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
    for j in range(len(to_mutate)):
        for i in range(len(to_mutate[j])):
            # print("bef", to_mutate[j][i])
            # print("len", len(to_mutate[j][i]))
            index = np.random.randint(0, len(to_mutate[j][i]))
            # print("bef1", to_mutate[j][i][index])
            if to_mutate[j][i][index] == 0:
                to_mutate[j][i][index] = '1'
            elif to_mutate[j][i][index] == 1:
                to_mutate[j][i][index] = '0'
            # print(to_mutate[j][i])

    new_population_bin = to_mutate + not_to_mutate
    # print(new_population_bin)
    # print("new pop")

    new_population = []
    for i in range(len(population)):
        # print(''.join([str(elem) for elem in new_population_bin[i]]))
        new_el = []
        # print(new_population_bin[i])
        for elem in population[i]:
            # str_bin = ''.join(str(elem))
            # print(elem)
            str_bin = ''.join([str(e) for e in elem])
            # print(str_bin)
            int_val = int(str_bin, 2)
            new_el.append(int_val)
        new_population.append(new_el)

    return new_population


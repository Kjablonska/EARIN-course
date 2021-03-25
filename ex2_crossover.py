import numpy as np
import ctypes
from codecs import decode
import struct
from ast import literal_eval

dimensions = 3
d = 3
A = np.asarray([[-2, 1, 0], [1, -2, 1], [0, 1, -2]])
b = np.asarray([-14, 14, -2])
c = -23.5
population_size = 50
crossover_prob = 0.9

def create_parents_tuples(population):
    size = len(population)
    parents = []

    i = 0
    size = len(population)
    while i < size:
        parent1 = population[i]
        population.pop(i)
        parent2_index = np.random.randint(0, size - 1)
        parent2 = population[parent2_index]
        population.pop(parent2_index)
        parents.append((parent1, parent2))
        size = size - 2     # Because we removed 2 parents from the parents list.
        i = i + 1

    return parents

def crossover_chromosomes(p_t):
    p1, p2 = p_t
    p1_bin = []
    p2_bin = []

    for i in p1:
        p1_bin.append(bin(i))

    for i in p2:
        p2_bin.append(bin(i))

    ch1 = []
    ch2 = []

    size = len(p1) # len(p1) == len(p2)
    crossover_point = np.random.randint(0, size)
    # print(size, crossover_point, p1_bin, p2_bin)

    i = 0
    while i < crossover_point:
        v1 = p1_bin[i]
        v2 = p2_bin[i]

        ch1.append(v1)
        ch2.append(v2)
        i= i + 1
    # print(i)

    j = crossover_point
    while j < size:
        v1 = p1_bin[j]
        v2 = p2_bin[j]

        ch1.append(v2)
        ch2.append(v1)
        j= j + 1
    # print(ch1, ch2)

    return ch1, ch2


def crossover(population):
    crossovered_species = []
    parents_tuples = create_parents_tuples(population)

    for p_t in parents_tuples:
        if np.random.uniform(0, 1) <= crossover_prob:
            # Crossover current tuple.
            ch1, ch2 = crossover_chromosomes(p_t)
            crossovered_species.append(ch1)
            crossovered_species.append(ch2)
        else:
            # Add current tuple without crossing.
            ch1, ch2 = p_t
            crossovered_species.append([bin(e) for e in ch1])
            crossovered_species.append([bin(e) for e in ch2])
    # print(crossovered_species)
    return crossovered_species



# def choose_chromosomes_to_crossover(population):
#     not_to_crossover = []
#     to_crossover = []
#     for chromosome in population:
#         if np.random.uniform(0, 1) < crossover_prob:
#             to_crossover.append(np.asarray(chromosome))
#         else:
#             not_to_crossover.append(np.asarray(chromosome))
#     return to_crossover, not_to_crossover


# def crossover(population):
#     crossovered_species = []
#     to_crossover, not_to_crossover = choose_chromosomes_to_crossover(population)

#     for el in not_to_crossover:
#         crossovered_species.append([bin(e) for e in el])

#     if len(to_crossover)%2 != 0:
#         tmp = to_crossover.pop()
#         crossovered_species.append([bin(e) for e in tmp])

#     p0 = 0
#     p1 = 1
#     while p1 < len(to_crossover):
#         ch1, ch2 = crossover_chromosomes(to_crossover[p0], to_crossover[p1])
#         crossovered_species.append(ch1)
#         crossovered_species.append(ch2)
#         p0 += 2
#         p1 += 2

#     return crossovered_species
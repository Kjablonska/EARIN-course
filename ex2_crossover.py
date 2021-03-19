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
mutation_prob = 0.05
iterations = 1000

def choose_chromosomes_to_crossover(population):
    not_to_crossover = []
    to_crossover = []
    for chromosome in population:
        if np.random.uniform(0, 1) < crossover_prob:
            to_crossover.append(np.asarray(chromosome))
        else:
            not_to_crossover.append(np.asarray(chromosome))
    return to_crossover, not_to_crossover

def crossover_chromosomes(p1, p2):
    p1_bin = list(bin(el) for el in p1)
    p2_bin = list(bin(el) for el in p2)

    child1 = p1_bin
    child2 = p2_bin
    ch1 = []
    ch2 = []

    for el in range(len(p1_bin)):
        child1 = list(p1_bin[el])
        child2 = list(p2_bin[el])
        crossover_point = max(len(child1), len(child2)) / 2

        i = min(len(child1), len(child2)) - 1
        while i > crossover_point:
            v_a = child1[i]
            v_b = child2[i]

            child1[i] = v_b
            child2[i] = v_a
            i = i - 1

        ch1.append(child1)
        ch2.append(child2)
    # print(ch1, ch2)
    return ch1, ch2


def crossover(population):
    crossovered_species = []
    to_crossover, not_to_crossover = choose_chromosomes_to_crossover(population)

    i = 0
    j = 1
    while len(crossovered_species) < population_size:
        if j > (len(to_crossover) - 1):
            j = 0
        if i >  (len(to_crossover) - 1):
            i = 0
        child_a, child_b = crossover_chromosomes(to_crossover[i], to_crossover[j])
        crossovered_species.append(list(child_a))
        crossovered_species.append(list(child_b))
        i += 1
        j += 1

    # Adding not_to_crossover chromosomes to crossovered_species.
    for i in range(len(not_to_crossover)):
        for elem in not_to_crossover[i]:
            crossovered_species.append(list(bin(elem)))

    # print(crossovered_species)

    # Corssovered species is a list of binary vectors.
    return crossovered_species

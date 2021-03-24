import numpy as np
from codecs import decode
import struct

mutation_prob = 0.05

def mutate_chromosome(population):
    for chromosome in population:
        for el in chromosome:
            # We need to start iterating over each element without taking into account '-0b' and '0b'.
            if el[0] == '-':
                low = 3
            else:
                low = 2

            for i in range(low, len(el)):
                if np.random.uniform(0, 1) < mutation_prob:
                    bin_el = list(el)
                    # print("bef", el, bin_el[i], i)
                    if bin_el[i] == '0':
                        bin_el[i] = '1'
                    elif bin_el[i] == '1':
                        bin_el[i] = '0'
                    el = ''.join([str(e) for e in bin_el])
                    # print("after", el, bin_el[i])

    return population

def mutate(population):
    population = mutate_chromosome(population)
    new_population = []
    for chromosome in population:
        new_population.append([int(x, 2) for x in chromosome])

    return new_population
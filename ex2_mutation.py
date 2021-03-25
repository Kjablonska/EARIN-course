import numpy as np
from codecs import decode
import struct

mutation_prob = 0.05

def mutate_chromosome(population):
    for chromosome in population:
        for el in chromosome:
            if el[0] != '-':
                el = ' ' + el

            for i in range(0, len(el) - 1):
                if np.random.uniform(0, 1) < mutation_prob:
                    bin_el = list(el)
                    if bin_el[i] == '0':
                        bin_el[i] = '1'
                    elif bin_el[i] == '1':
                        bin_el[i] = '0'
                    if bin_el[i] == ' ':
                        bin_el[i] = '-'
                    elif bin_el[i] == '-':
                        bin_el[i] = ' '
                    el = ''.join([str(e) for e in bin_el])

    return population


def mutate(population):
    population = mutate_chromosome(population)
    new_population = []
    for chromosome in population:
        new_population.append([int(x, 2) for x in chromosome])

    return new_population

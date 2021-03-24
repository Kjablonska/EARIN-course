import numpy as np
from codecs import decode
import struct


def mutate_chromosome(population, _mutation_probability):
    for chromosome in population:
        for el in chromosome:
            # We need to start iterating over each element without taking into account '-0b' and '0b'.
            if el[0] == '-':
                low = 2
            else:
                low = 1

            if np.random.uniform(0, 1) < _mutation_probability:
                for i in range(0, len(el)):
                    if i == low or i == low - 1:
                        continue
                    bin_el = list(el)
                    # print("bef", el, bin_el[i], i)
                    if bin_el[i] == '0':
                        bin_el[i] = '1'
                    elif bin_el[i] == '1':
                        bin_el[i] = '0'
                    elif bin_el[i] == '-':
                        bin_el[i] = ' '
                    elif bin_el[i] == ' ':
                        bin_el[i] = '-'
                    el = ''.join([str(e) for e in bin_el])
                    # print("after", el, bin_el[i])

    return population

def mutate(population, _mutation_probability):
    population = mutate_chromosome(population, _mutation_probability)
    new_population = []
    for chromosome in population:
        new_population.append([int(x, 2) for x in chromosome])

    return new_population
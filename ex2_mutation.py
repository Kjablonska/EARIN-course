import numpy as np
from codecs import decode
import struct

mutation_prob = 0.05

def mutate_chromosome(chromosome):
    mut = []
    for gen in chromosome:
        el = list(gen)
        low = 0
        if el[0] == '-':
            low = 1

        # Mutate random gen in each chromosome.
        i = np.random.randint(low, len(el))
        if el[i] == '0':
            el[i] = '1'
        elif el[i] == '1':
            el[i] = '0'
        el = ''.join([str(tmp) for tmp in el])
        mut.append(el)

    return mut

def mutate(population):
    new_population = []
    for chromosome in population:
        if np.random.uniform(0, 1) <= mutation_prob:
            mutated = mutate_chromosome(chromosome)
            # new_population.append(np.array(mutated))
            new_population.append(np.asarray([int(x, 2) for x in mutated]))
        else:
            # new_population.append(chromosome)
            new_population.append(np.asarray([int(x, 2) for x in chromosome]))

    return np.asarray(new_population)

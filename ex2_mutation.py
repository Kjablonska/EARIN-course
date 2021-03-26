import numpy as np
from codecs import decode
import struct

mutation_prob = 0.05

# Mutation of chromosome using XOR binary operator.
def mutate_chromosome(chromosome):
    mutated = []

    to_mutate_index = np.random.randint(0, len(chromosome))
    for index in range(len(chromosome)):
        if to_mutate_index == index:
            gen = chromosome[index]
            bit_to_mutate = 2**(np.random.randint(0, len(gen)))
            if gen[0] == '-':
                bit_to_mutate = 2**(np.random.randint(0, len(gen) - 1))
            mutated.append(np.binary_repr(int(gen, 2)^bit_to_mutate))
        else:
            mutated.append(chromosome[index])
    return mutated

def mutate(population):
    new_population = []
    for chromosome in population:
        if np.random.uniform(0, 1) <= mutation_prob:
            mutated = mutate_chromosome(chromosome)
            new_population.append(np.asarray([int(x, 2) for x in mutated]))
        else:
            new_population.append(np.asarray([int(x, 2) for x in chromosome]))

    return np.asarray(new_population)
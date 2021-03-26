import numpy as np


def mutate_chromosome(chromosome, _d):
    mutated = []
    to_mutate_index = np.random.randint(0, len(chromosome))
    for index in range(len(chromosome)):
        if to_mutate_index == index:

            gen = chromosome[index]
            sign = np.random.randint(0, 2) # Generates random integer between [0, 2)

            # sign == 0 => number is positive.
            if (sign == 0):
                bit_to_mutate = 2**(np.random.randint(0, _d-1))
            else:
                bit_to_mutate = (-1)*(2**(np.random.randint(0, _d)))

            # print(np.binary_repr(bit_to_mutate))
            mutated.append(np.binary_repr(int(gen, 2)^bit_to_mutate))
            # print(chromosome[index], mutated[index])
        else:
            mutated.append(chromosome[index])
    # print(chromosome, mutated)
    return mutated


def mutate(population, _mutation_probability, _d):
    new_population = []
    for chromosome in population:
        if np.random.uniform(0, 1) <= _mutation_probability:
            mutated = mutate_chromosome(chromosome, _d)
            new_population.append(np.asarray([int(x, 2) for x in mutated]))
        else:
            new_population.append(np.asarray([int(x, 2) for x in chromosome]))

    return np.asarray(new_population)

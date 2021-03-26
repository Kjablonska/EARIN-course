import numpy as np


def mutate_chromosome(chromosome):
    d = 3
    mutated = []
    to_mutate_index = np.random.randint(0, len(chromosome))

    for index in range(len(chromosome)):
        if to_mutate_index == index:
            gen = chromosome[index]
            bit_to_mutate = np.random.randint(-2**d, 2**d)
            gen.zfill(len(np.binary_repr(bit_to_mutate)))

            el = list(gen)
            if(el[bit_to_mutate] == '0'):
                bit_to_mutate= '1'
            elif el[bit_to_mutate] == '1':
                bit_to_mutate = '0'

            g = ''.join(gen)
            mutated.append(g)
            # bit_to_mutate = 2**(np.random.randint(0, len(gen)))
            # if gen[0] == '-':
            #     bit_to_mutate = 2**(np.random.randint(0, len(gen) - 1))
            # mutated.append(np.binary_repr(int(gen, 2) ^ bit_to_mutate))
        else:
            mutated.append(chromosome[index])

    return mutated


def mutate(population, _mutation_probability):
    new_population = []
    for chromosome in population:
        if np.random.uniform(0, 1) <= _mutation_probability:
            mutated = mutate_chromosome(chromosome)
            new_population.append(np.asarray([int(x, 2) for x in mutated]))
        else:
            new_population.append(np.asarray([int(x, 2) for x in chromosome]))

    return np.asarray(new_population)

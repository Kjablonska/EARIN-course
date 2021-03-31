import numpy as np


def mutate_chromosome(chromosome, _mutation_probability, _d):
    for index in range(len(chromosome)):
        el = list(chromosome[index])
        mut = []
        for bin in el:
            if np.random.uniform(0, 1) <= _mutation_probability:
                if bin == '1':
                    bin = '0'
                elif bin == '0':
                    bin = '1'
                if bin == '-':
                    bin = ' '
            mut.append(bin)
        chromosome[index] = ''.join(mut)

    return chromosome


def mutate(population, _mutation_probability, _d):
    new_population = []
    for chromosome in population:
        mutated = mutate_chromosome(chromosome, _mutation_probability, _d)
        new_population.append(np.asarray([int(x, 2) for x in mutated]))

    return np.asarray(new_population)

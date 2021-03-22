import numpy as np
from codecs import decode
import struct

mutation_prob = 0.05

def choose_chromosomes_to_mutate(population):
    to_mutate = []
    not_to_mutate = []

    for chromosome in population:
        if np.random.uniform(0, 1) < mutation_prob:
            to_mutate.append(chromosome)
        else:
            not_to_mutate.append(chromosome)
    return to_mutate, not_to_mutate


def mutate_chromosome(population):
    for j in range(len(population)):
        for i in range(len(population[j])):
            # print("to mutate", population[j], len(population[j][i]))
            for index in range(len(population[j][i])):
                if np.random.uniform(0, 1) <= mutation_prob:
                    # print("bef", population[j][i][index])
                    if population[j][i][index] == '0':
                        population[j][i][index] = '1'
                    elif population[j][i][index] == '1':
                        population[j][i][index] = '0'
                    if population[j][i][index] == ' ':
                        population[j][i][index] = '-'
                    elif population[j][i][index] == '-':
                        population[j][i][index] = ' '
                    # print("after", population[j][i][index])
    return population

def mutate(pop):
    population = mutate_chromosome(pop)
    # print(population)
    new_population = []
    for i in range(len(population)):
        new_el = []
        for elem in population[i]:
            str_bin = ''.join([str(e) for e in elem])
            int_val = int(str_bin, 2)
            new_el.append(int_val)
        new_population.append(new_el)

    return new_population

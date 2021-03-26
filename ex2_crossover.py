import numpy as np

dimensions = 3
d = 3
A = np.asarray([[-2, 1, 0], [1, -2, 1], [0, 1, -2]])
b = np.asarray([-14, 14, -2])
c = -23.5
population_size = 50
crossover_prob = 0.9

def create_parents_tuples(population):
    size = len(population)
    parents = []

    i = 0
    size = len(population)
    while i < size:
        parent1 = population[i]
        population.pop(i)
        parent2_index = np.random.randint(0, size - 1)
        parent2 = population[parent2_index]
        population.pop(parent2_index)
        parents.append((parent1, parent2))
        size = size - 2     # Because we removed 2 parents from the parents list.
        i = i + 1

    return parents

def crossover_chromosomes(p_t):
    p1, p2 = p_t
    p1_bin = []
    p2_bin = []

    for i in p1:
        p1_bin.append(np.binary_repr(i))

    for i in p2:
        p2_bin.append(np.binary_repr(i))

    ch1 = []
    ch2 = []
    size = len(p1)              # len(p1) == len(p2)
    crossover_point = np.random.randint(1, size)

    i = 0
    while i < crossover_point:
        v1 = p1_bin[i]
        v2 = p2_bin[i]

        ch1.append(v1)
        ch2.append(v2)
        i= i + 1

    j = crossover_point
    while j < size:
        v1 = p1_bin[j]
        v2 = p2_bin[j]

        ch1.append(v2)
        ch2.append(v1)
        j= j + 1

    return ch1, ch2


def crossover(population):
    crossovered_species = []
    parents_tuples = create_parents_tuples(population)

    for p_t in parents_tuples:
        if np.random.uniform(0, 1) <= crossover_prob:
            # Crossover current tuple of parents and replace it with created offsprings.
            ch1, ch2 = crossover_chromosomes(p_t)
            crossovered_species.append(ch1)
            crossovered_species.append(ch2)
        else:
            # Add current tuple of parents without crossing.
            ch1, ch2 = p_t
            crossovered_species.append([np.binary_repr(e) for e in ch1])
            crossovered_species.append([np.binary_repr(e) for e in ch2])

    return crossovered_species

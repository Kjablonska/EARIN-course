import numpy as np

def create_parents_tuples(population):
    size = len(population)
    parents = []

    i = 0
    size = len(population)
    while i < size:
        parent1 = population[i]
        population.pop(i)
        parent2_index = np.random.randint(0, size - 1)  # Substraction 1 from size beacuse one element was removed from population.
        parent2 = population[parent2_index]
        population.pop(parent2_index)
        parents.append((parent1, parent2))
        size = size - 2    # Because we removed 2 parents from the parents list.
        i = i + 1

    return parents

def crossover_chromosomes(p_t):
    p1, p2 = p_t
    p1_bin = []
    p2_bin = []
    ch1 = []
    ch2 = []

    # Convert parents to binary vectors.
    for i in p1:
        p1_bin.append(np.binary_repr(i))

    for i in p2:
        p2_bin.append(np.binary_repr(i))

    size = len(p1)              # len(p1) == len(p2)
    crossover_point = np.random.randint(1, size)

    i = 0
    while i < crossover_point:
        v1 = p1_bin[i]
        v2 = p2_bin[i]
        ch1.append(v1)
        ch2.append(v2)
        i = i + 1

    j = crossover_point
    while j < size:
        v1 = p1_bin[j]
        v2 = p2_bin[j]
        ch1.append(v2)
        ch2.append(v1)
        j = j + 1

    return ch1, ch2


def crossover(population, _cross_probability):
    crossovered_species = []

    # If population is not even.
    if len(population)%2 != 0:
        odd_parent = population.pop(np.random.randint(0, len(population)))
        crossovered_species.append([np.binary_repr(p) for p in odd_parent])

    parents_tuples = create_parents_tuples(population)

    for p_t in parents_tuples:
        if np.random.uniform(0, 1) <= _cross_probability:
            # Crossover current tuple of parents and replace it with created offsprings.
            ch1, ch2 = crossover_chromosomes(p_t)
            crossovered_species.append(ch1)
            crossovered_species.append(ch2)
        else:
            # Add current tuple of parents without crossing.
            ch1, ch2 = p_t
            crossovered_species.append([np.binary_repr(gen) for gen in ch1])
            crossovered_species.append([np.binary_repr(gen) for gen in ch2])

    return crossovered_species

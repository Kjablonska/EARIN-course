import numpy as np

dimensions = 3
d = 3
A = np.asarray([[-2, 1, 0], [1, -2, 1], [0, 1, -2]])
b = np.asarray([-14, 14, -2])
c = -23.5
population_size = 50
crossover_prob = 0.9
mutation_prob = 0.05
iterations = 1000

not_to_crossover = []
to_crossover = []

crossover_tuples = []

def choose_chromosomes_to_crossover(population):
    # We need to remove parents from population_arr before finding spieces to crossover.
    for chromosome in population:
        if np.random.uniform(0, 1) < crossover_prob:
            to_crossover.append(chromosome)
        else:
            not_to_crossover.append(chromosome)


def create_crossover_tuples():
    to_crossover = list(enumerate(to_crossover))
    while to_crossover:
        chromosome_to_crossover_index, chromosome_to_crossover = to_crossover.pop()

        if not to_crossover:
            not_to_crossover.append(chromosome_to_crossover)
            break

        crossover_buddy_index, crossover_buddy = np.random.choice(to_crossover)
        to_crossover = list(filter(lambda value: value[0] != crossover_buddy_index, to_crossover))
        crossover_tuples.append((chromosome_to_crossover, crossover_buddy))
    return crossover_tuples


def crossover_chromosomes(parents):
    p1 = parents[0]
    p2 = parents[1]
    p1_bin = list(np.binary_repr(p1))
    p2_bin = list(np.binary_repr(p2))

    child1 = p1_bin
    child2 = p2_bin

    crossover_point = p1_bin.len() / 2

    for index in range(crossover_point):
        # Values on index
        value_a = child1[index]
        value_b = child2[index]
        # Values for swap
        index_of_value_b_in_a = child1.index(value_b)
        index_of_value_a_in_b = child2.index(value_a)
        # Save values
        child1[index_of_value_b_in_a] = value_a
        child2[index_of_value_a_in_b] = value_b
        # Change values
        child1[index] = value_b
        child2[index] = value_a
        return child1, child2



def crossover():
    crossovered_species = []
    for crossover_tuple in crossover_tuples:
        child_a, child_b = crossover_chromosomes(
            crossover_tuple
        )
        crossovered_species.append(child_a)
        crossovered_species.append(child_b)

    print(crossovered_species)
    return crossovered_species
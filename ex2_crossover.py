import numpy as np
import ctypes
from codecs import decode
import struct
from ast import literal_eval

dimensions = 3
d = 3
A = np.asarray([[-2, 1, 0], [1, -2, 1], [0, 1, -2]])
b = np.asarray([-14, 14, -2])
c = -23.5
population_size = 50
crossover_prob = 0.9
mutation_prob = 0.05
iterations = 1000

def choose_chromosomes_to_crossover(population):
    not_to_crossover = []
    to_crossover = []
    for chromosome in population:
        if np.random.uniform(0, 1) < crossover_prob:
            to_crossover.append(chromosome)
        else:
            not_to_crossover.append(chromosome)
    return to_crossover, not_to_crossover

def create_crossover_tuples(to_crossover, not_to_crossover):
    crossover_tuples = []
    to_crossover = list(enumerate(to_crossover))
    while to_crossover:
        chromosome_to_crossover_index, chromosome_to_crossover = to_crossover.pop()

        if not to_crossover:
            not_to_crossover.append(chromosome_to_crossover)
            break

        np.random.shuffle(to_crossover)
        crossover_buddy_index, crossover_buddy = to_crossover.pop()
        to_crossover = list(filter(lambda value: value[0] != crossover_buddy_index, to_crossover))
        crossover_tuples.append((chromosome_to_crossover, crossover_buddy))
    return crossover_tuples


def crossover_chromosomes(parents):
    p1 = parents[0]
    p2 = parents[1]

    p1_bin = list(bin(el) for el in p1)
    p2_bin = list(bin(el) for el in p2)

    child1 = p1_bin
    child2 = p2_bin

    crossover_point = int(len(p1_bin) / 2)

    for i in range(crossover_point):
        i += 2
        v_a = child1[i]
        v_b = child2[i]

        child1[i] = v_b
        child2[i] = v_a

    return child1, child2


def crossover(population):
    crossovered_species = []
    to_crossover, not_to_crossover = choose_chromosomes_to_crossover(population)
    crossover_tuples = create_crossover_tuples(to_crossover, not_to_crossover)

    for crossover_tuple in crossover_tuples:
        child_a, child_b = crossover_chromosomes(crossover_tuple)
        crossovered_species.append(list(child_a))
        crossovered_species.append(list(child_b))

    # Adding not_to_crossover chromosomes to crossovered_species.
    for i in range(len(not_to_crossover)):
        new_el = []
        for elem in not_to_crossover[i]:
            new_el.append(bin(elem))
        crossovered_species.append(new_el)

    # Corssovered species is a list of binary vectors.
    return crossovered_species



# def bin_to_float(b):
#     """ Convert binary string to a float. """
#     bf = int_to_bytes(int(b, 2), 8)  # 8 bytes needed for IEEE 754 binary64.
#     # bf = (b).to_bytes(2, byteorder='big')
#     return struct.unpack('>d', bf)[0]


# def int_to_bytes(n, length):  # Helper function
#     """ Int/long to byte string.

#         Python 3.2+ has a built-in int.to_bytes() method that could be used
#         instead, but the following works in earlier versions including 2.x.
#     """
#     return decode('%%0%dx' % (length << 1) % n, 'hex')[-length:]


# def float_to_bin(value):  # For testing.
#     """ Convert float to 64-bit binary string. """
#     [d] = struct.unpack(">Q", struct.pack(">d", value))
#     return '{:064b}'.format(d)
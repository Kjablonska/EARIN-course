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

def choose_chromosomes_to_crossover(population):
    not_to_crossover = []
    to_crossover = []
    for chromosome in population:
        if np.random.uniform(0, 1) <= crossover_prob:
            to_crossover.append(np.asarray(chromosome))
        else:
            not_to_crossover.append(np.asarray(chromosome))
    return to_crossover, not_to_crossover

def crossover_chromosomes(p1, p2):

    p1_bin, p2_bin = getBinaryRepresentation(p1, p2)
    ch1 = []
    ch2 = []

    for el in range(len(p1_bin)):
        child1 = list(p1_bin[el])
        child2 = list(p2_bin[el])

        # Crossover point starts from index 1 because we don't want to change signs.
        crossover_point = np.random.randint(1, len(child1))
        i = 0
        while i < crossover_point:
            v_a = child1[i]
            v_b = child2[i]

            child1[i] = v_b
            child2[i] = v_a
            i=i+1

        ch1.append(child1)
        ch2.append(child2)
    return ch1, ch2


def crossover(population):
    crossovered_species = []
    to_crossover, not_to_crossover = choose_chromosomes_to_crossover(population)

    # Adding not_to_crossover chromosomes to crossovered_species.
    for i in range(len(not_to_crossover)):
        new_el = []
        for el in not_to_crossover[i]:
            if el < 0:
                x1 = '-' + bin(el)[3:]
            elif el >= 0:
                x1 = ' ' + bin(el)[2:]
            new_el.append(list(x1))
        crossovered_species.append(new_el)

    i = 0
    j = 1
    while len(crossovered_species) < population_size and len(to_crossover) != 0:
        if j > (len(to_crossover) - 1):
            j = 0
        if i >  (len(to_crossover) - 1):
            i = 0
        child_a, child_b = crossover_chromosomes(to_crossover[i], to_crossover[j])
        # print("crossed", i, j)
        crossovered_species.append(list(child_a))
        crossovered_species.append(list(child_b))
        i = i + 2
        j = j + 2

    if population_size != len(crossovered_species):
        crossovered_species.pop(1)

    return crossovered_species

def getBinaryRepresentation(p1, p2):
    p1_bin = []
    p2_bin = []

    # Removal of '0b' after conversion to binary and addition of padding.
    for i in range(len(p1)):
        el1 = p1[i]
        el2 = p2[i]
        el1_bin = bin(el1)
        el2_bin = bin(el2)

        if el1 < 0:
            x1 = el1_bin[3:]
        elif el1 >= 0:
            x1 = el1_bin[2:]

        if el2 < 0:
            x2 = el2_bin[3:]
        elif el2 >= 0:
            x2 = el2_bin[2:]

        fill = max(len(x1), len(x2))

        if (el1) < 0:
            x1 = '-' + x1.zfill(fill)
        elif el1 >=0:
            x1 = ' ' + x1.zfill(fill)

        if (el2) < 0:
            x2 = '-' + x2.zfill(fill)
        elif el2 >=0:
            x2 = ' ' + x2.zfill(fill)

        p1_bin.append(x1)
        p2_bin.append(x2)

    return p1_bin, p2_bin
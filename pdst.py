#!/usr/bin/env python

from __future__ import print_function, division
import os
from itertools import product, islice
import math

from revp import read_fasta
from hamm import hamming


def p_distance(s1, s2):
    return hamming(s1, s2) / len(s1)


def distance_matrix(seqs):
    output = []

    distances = []
    for a, b in product(seqs.values(), repeat=2):
        distances.append(round(p_distance(a, b), 3))

    reshape = iter(distances)
    for i in range(int(math.ceil(len(distances) / len(seqs)))):
        output.append(tuple(islice(reshape, len(seqs))))
    return output


if __name__ == "__main__":
    with open(os.path.join('data', 'rosalind_pdst.txt')) as dataset:
        seqs = read_fasta(dataset)
        for row in distance_matrix(seqs):
            print(*row)

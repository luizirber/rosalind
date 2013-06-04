#!/usr/bin/env python

from __future__ import print_function
import os
import operator
from functools import reduce

from prot import prepare_codon_table


if __name__ == "__main__":
    with open(os.path.join('data', 'rosalind_mrna.txt')) as dataset:
        protein_string = dataset.read().rstrip()
        codon_table = prepare_codon_table(os.path.join('data', 'codon_table'))

        stop_codons = [c for c in codon_table if codon_table[c] == 'Stop']

        possibilities = []
        for p in protein_string:
            possibilities.append([(p, c) for c in codon_table
                                  if codon_table[c] == p])

        print((len(stop_codons) * reduce(operator.mul,
                                         map(len, possibilities))) % 1000000)

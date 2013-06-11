#!/usr/bin/env python

from __future__ import print_function
import os

from prot import prepare_codon_table


def prepare_mass_table(filename):
    table = prepare_codon_table(filename)
    return {k: round(float(table[k]), 5) for k in table}


def protein_weight(protein):
    mass_table = prepare_mass_table(os.path.join('data', 'monoisotopic_mass'))
    return sum(mass_table[p] for p in protein)


if __name__ == "__main__":
    with open(os.path.join('data', 'rosalind_prtm.txt')) as dataset:
        print(round(protein_weight(dataset.read().rstrip()), 3))

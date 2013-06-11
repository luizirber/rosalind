#!/usr/bin/env python

from __future__ import print_function
import os

from conv import multiplicity
from prtm import protein_weight


def all_substrings(string):
    for i in range(len(string)):
        if i != len(string) - 1:
            yield string[:i + 1]
        yield string[-i:]


def match_spectrum(proteins, rset):
    largest = 0
    max_protein = None
    for protein in proteins:
        pset = [protein_weight(p) for p in all_substrings(protein)]
        most, _ = multiplicity(rset, pset)
        if most >= largest:
            largest = most
            max_protein = protein
    return largest, max_protein


if __name__ == "__main__":
    with open(os.path.join('data', 'rosalind_prsm.txt')) as dataset:
        n = int(dataset.readline().rstrip())
        proteins = [dataset.readline().rstrip() for i in range(n)]
        rset = [round(float(r.rstrip()), 5) for r in dataset.readlines()]

    print(*match_spectrum(proteins, rset), sep='\n')

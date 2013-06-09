#!/usr/bin/env python

from __future__ import print_function
import os


def dna_count(dna, order='ACGT'):
    return [dna.count(o) for o in order]


if __name__ == "__main__":
    with open(os.path.join('data', 'rosalind_dna.txt')) as dataset:
        print(*dna_count(dataset.read()))

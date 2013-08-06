#!/usr/bin/env python

from __future__ import print_function
import os
from math import factorial

from revp import read_fasta


def maximum_matchings(seq):
    min_gc, max_gc = sorted([seq.count('G'), seq.count('C')])
    min_au, max_au = sorted([seq.count('A'), seq.count('U')])
    return (factorial(max_gc) // factorial(max_gc - min_gc) *
            factorial(max_au) // factorial(max_au - min_au))

if __name__ == "__main__":
    with open(os.path.join('data', 'rosalind_mmch.txt')) as dataset:
        seq = read_fasta(dataset).popitem()[1]
    print(maximum_matchings(seq))

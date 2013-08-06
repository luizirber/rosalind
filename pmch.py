#!/usr/bin/env python

from __future__ import print_function
import os
from math import factorial

from revp import read_fasta


def perfect_matchings(seq):
    return factorial(seq.count('G')) * factorial(seq.count('A'))


if __name__ == "__main__":
    with open(os.path.join('data', 'rosalind_pmch.txt')) as dataset:
        seq = read_fasta(dataset).popitem()[1]
    print(perfect_matchings(seq))

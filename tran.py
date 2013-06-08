#!/usr/bin/env python

from __future__ import print_function, division
import os

from revp import read_fasta


def tr_ratio(s1, s2):
    transitions = 0
    transversions = 0
    for c1, c2 in zip(s1, s2):
        if c1 + c2 in ('AG', 'GA', 'CT', 'TC'):
            transitions += 1
        elif c1 + c2 in ('CA', 'AC', 'AT', 'TA', 'TG', 'GT', 'CG', 'GC'):
            transversions += 1
    return transitions / transversions


if __name__ == "__main__":
    with open(os.path.join('data', 'rosalind_tran.txt')) as dataset:
        seqs = read_fasta(dataset)
        print(round(tr_ratio(seqs.popitem()[1], seqs.popitem()[1]), 3))

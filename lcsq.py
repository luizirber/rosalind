#!/usr/bin/env python

from __future__ import print_function
import os
import sys
sys.setrecursionlimit(10000)

from revp import read_fasta
from lgis import lcs


if __name__ == "__main__":
    with open(os.path.join('data', 'rosalind_lcsq.txt')) as dataset:
        seqs = read_fasta(dataset)
    s1 = seqs.popitem()[1]
    s2 = seqs.popitem()[1]
    print(*lcs(s1, s2), sep='')

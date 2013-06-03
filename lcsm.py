#!/usr/bin/env python

from __future__ import print_function
import os
from functools import reduce

from revp import read_fasta


def longest_common_substring(s1, s2):
    ''' See
    http://en.wikipedia.org/wiki/Longest_common_substring_problem#Pseudocode
    for more details '''

    L = {}
    z = 0

    for i, c1 in enumerate(s1):
        for j, c2 in enumerate(s2):
            if c1 == c2:
                L[(i, j)] = L.get((i - 1, j - 1), 0) + 1

                if L[(i, j)] > z:
                    z = L[(i, j)]
                    ret = s1[i - z + 1:i + 1]
    return ret


if __name__ == "__main__":
    with open(os.path.join('data', 'rosalind_lcsm.txt')) as dataset:
        seqs = read_fasta(dataset)
        print(reduce(longest_common_substring, set(seqs.values())))

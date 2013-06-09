#!/usr/bin/env python

from __future__ import print_function, division
import os

from revp import read_fasta


def failure_array(seq):
    m = len(seq)
    output = m * [0]
    j = output[0]
    for i in range(1, m):
        while j > 0 and seq[i] != seq[j]:
            j = output[j - 1]
        if seq[i] == seq[j]:
            j += 1
        output[i] = j
    return output


if __name__ == "__main__":
    with open(os.path.join('data', 'rosalind_kmp.txt')) as dataset:
        seqs = read_fasta(dataset)
    print(*failure_array(seqs.popitem()[1]))

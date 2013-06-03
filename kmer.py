#!/usr/bin/env python

from __future__ import print_function
import os

from revp import read_fasta
from subs import substring_find
from lexf import lexf_order


def kmer_composition(dna_string):
    output = []
    for p in lexf_order(4, 'ACGT'):
        pos = list(substring_find(dna_string, ''.join(p)))
        output.append(str(len(pos)))
    return output


if __name__ == "__main__":
    with open(os.path.join('data', 'rosalind_kmer.txt')) as dataset:
        seqs = read_fasta(dataset)
        dna_string = seqs.popitem(last=False)[1]
        print(*kmer_composition(dna_string))

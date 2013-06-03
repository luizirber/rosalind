#!/usr/bin/env python

from __future__ import print_function
import os

from revp import read_fasta


def gc_content(seq):
    count = seq.count('C') + seq.count('G')
    return float(count) / len(seq)


if __name__ == "__main__":
    with open(os.path.join('data', 'rosalind_gc.txt')) as dataset:
        seqs = read_fasta(dataset)
        gc = {k: gc_content(seqs[k]) for k in seqs}
        maxes = max(gc)

        print(maxes[1:], "\n%.2f%%" % (round(gc[maxes] * 100, 2)))

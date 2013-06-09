#!/usr/bin/env python

from __future__ import print_function, division
import os
from collections import Counter

from revp import read_fasta
from revc import reverse_complement
from hamm import hamming


def correct_errors(seqs):
    corrections = []
    c = Counter(seqs)

    correct = [item for item in c if c[item] >= 2]
    reverse = {reverse_complement(s) for s in correct}
    seqset = set(correct)

    for s in [item for item in c if c[item] < 2]:
        if s not in reverse:
            for fix in (f for f in seqset | reverse if hamming(s, f) == 1):
                corrections.append((s, fix))

    return corrections


if __name__ == "__main__":
    with open(os.path.join('data', 'rosalind_corr.txt')) as dataset:
        seqs = read_fasta(dataset)
        for fix in correct_errors([seqs[s] for s in seqs]):
            print(*fix, sep='->')

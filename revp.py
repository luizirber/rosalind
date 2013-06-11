#!/usr/bin/env python

from __future__ import print_function
import os
from collections import OrderedDict

from revc import reverse_complement


def read_fasta(fp):
    seqs = OrderedDict()
    current = None
    buff = []
    for line in fp:
        if line.startswith('>'):
            if current:
                seqs[current] = ''.join(buff).rstrip()
                buff = []
            current = line.rstrip()
        else:
            buff.append(line.rstrip())
    seqs[current] = ''.join(buff).rstrip()
    return seqs


def reverse_palindrome(dna):
    size = len(dna)
    for start in range(size):
        for length in range(4, 13):
            piece = dna[start:start + length]
            if len(piece) >= 4 and piece == reverse_complement(piece):
                yield (start + 1, length)


if __name__ == "__main__":
    with open(os.path.join('data', 'rosalind_revp.txt')) as dataset:
        seq = read_fasta(dataset)
        s = seq.popitem()[1]
        for i in reverse_palindrome(s):
            print(*i, sep=" ")

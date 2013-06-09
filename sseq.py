#!/usr/bin/env python

from __future__ import print_function, division
import os

from revp import read_fasta


def subsequence(s, t):
    output = []
    pos = 0
    for symbol in t:
        pos = s.find(symbol, pos)
        pos = pos + 1
        output.append(pos)
    return output


if __name__ == "__main__":
    with open(os.path.join('data', 'rosalind_sseq.txt')) as dataset:
        seqs = read_fasta(dataset)
        s = seqs.popitem(last=False)[1]
        t = seqs.popitem()[1]
        print(*subsequence(s, t))

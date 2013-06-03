#!/usr/bin/env python

from __future__ import print_function
import os

from revp import read_fasta


def adjacency_list(seqs):
    output = []
    for seq in seqs:
        seq_end = seqs[seq][-3:]
        adjs = set(seqs.keys())
        adjs.remove(seq)
        for adj in adjs:
            if seq_end == seqs[adj][:3]:
                output.append("%s %s" % (seq[1:], adj[1:]))
    return output


if __name__ == "__main__":
    with open(os.path.join('data', 'rosalind_grph.txt')) as dataset:
        seqs = read_fasta(dataset)
        print(*adjacency_list(seqs), sep="\n")

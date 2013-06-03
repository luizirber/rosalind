#!/usr/bin/env python

from __future__ import print_function
import os
from math import ceil

from revp import read_fasta
from subs import substring_find


def adjacency_list(seqs):
    vertex = set()
    for seq in seqs:
        seq_data = seqs[seq]
        overlap_seq = int(ceil(len(seq_data) / 2))

        adjs = set(seqs.keys())
        adjs.remove(seq)
        for adj in adjs:
            overlap = overlap_seq
            adj_data = seqs[adj]
            overlap_adj = int(ceil(len(adj_data) / 2))

            if overlap < overlap_adj:
                overlap = overlap_adj

            pos = list(substring_find(seq_data, adj_data[:overlap]))
            if pos:
                vertex.add((seq, adj, pos[-1]))
    return vertex


def superstring_pos(vertex):
    superstring = []
    for v in vertex:
        if not superstring:
            superstring.append((v[0], v[2]))
            superstring.append((v[1], None))

        remainder = vertex - set([v])
        for r in remainder:
            if r[0] == superstring[-1][0]:
                superstring[-1] = (r[0], r[2])
                superstring.append((r[1], None))
            elif r[1] == superstring[0][0]:
                superstring.insert(0, (r[0], r[2]))
    return superstring


def shortest_substring(seqs):
    vertex = adjacency_list(seqs)
    superstring = superstring_pos(vertex)

    output = []
    for k, pos in reversed(superstring):
        if pos:
            output.insert(0, seqs[k][:pos - 1])
        else:
            output.append(seqs[k])

    return "".join(output)


if __name__ == "__main__":
    with open(os.path.join('data', 'rosalind_long.txt')) as dataset:
        seqs = read_fasta(dataset)
        print(shortest_substring(seqs))

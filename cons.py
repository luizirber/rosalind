#!/usr/bin/env python

from __future__ import print_function
import os

from revp import read_fasta


def prof_matrix(strings):
    profs = dict.fromkeys('A C G T'.split(), None)
    size = len(strings[0])
    for s in strings:
        for i, c in enumerate(s):
            if not profs[c]:
                profs[c] = {i: 0 for i in range(size)}
            profs[c][i] = profs[c].get(i, 0) + 1
    return profs


def print_prof_matrix(pmat):
    for c in sorted(pmat):
        print("%s: %s" % (c, " ".join([str(v) for k, v in sorted(pmat[c].items())])))


def consensus(pmatrix):
    maxs = []
    for i in range(len(pmatrix['A'])):
        m = 0
        for k in pmatrix:
            if pmat[k][i] > m:
                m = pmat[k][i]
                mk = k
        maxs.append(mk)
    return "".join(maxs)


if __name__ == "__main__":
    with open(os.path.join('data', 'rosalind_cons.txt')) as dataset:
        seqs = read_fasta(dataset)
        pmat = prof_matrix([seqs[k] for k in seqs])
        print(consensus(pmat))
        print_prof_matrix(pmat)

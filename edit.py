#!/usr/bin/env python

from __future__ import print_function
import os

from revp import read_fasta


def edit_distance(s, t):
    ''' Graphical explanation at
    http://www.codeproject.com/Articles/13525/Fast-memory-efficient-Levenshtein-algorithm
    '''
    if s == t:
        return 0
    elif len(s) == 0:
        return len(t)
    elif len(t) == 0:
        return len(s)

    v0 = list(range(0, len(t) + 1))
    v1 = (len(t) + 1) * [0]

    for i in range(0, len(s)):
        v1[0] = i + 1

        for j in range(0, len(t)):
            cost = 0 if s[i] == t[j] else 1
            v1[j + 1] = min(v1[j] + 1, v0[j + 1] + 1, v0[j] + cost)

        v0 = v1[:]

    return v1[len(t)]


if __name__ == "__main__":
    with open(os.path.join('data', 'rosalind_edit.txt')) as dataset:
        seqs = read_fasta(dataset)
        s1, s2 = [seqs[k] for k in seqs]
        print(edit_distance(s1, s2))

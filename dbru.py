#!/usr/bin/env python

from __future__ import print_function
import os

from revc import reverse_complement

if __name__ == "__main__":
    with open(os.path.join('data', 'rosalind_dbru.txt')) as dataset:
        dna_set = set(s[:-1] for s in dataset)

    reverse_complements = {reverse_complement(s) for s in dna_set}
    dna_strings = dna_set | reverse_complements

    item = dna_strings.pop()
    k = len(item) - 1
    dna_strings.add(item)

    adj_list = {(r[0:k], r[1:k + 1]) for r in dna_strings}

    for adj in sorted(adj_list):
        print('(' + adj[0] + ', ' + adj[1] + ')')

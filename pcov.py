#!/usr/bin/env python

from __future__ import print_function
import os

from revc import reverse_complement


if __name__ == "__main__":
    with open(os.path.join('data', 'rosalind_pcov.txt')) as dataset:
        reads = {s.rstrip() for s in dataset}

    reverse_complements = {reverse_complement(s) for s in reads}
    dna_strings = reads | reverse_complements

    item = dna_strings.pop()
    k = len(item) - 1
    dna_strings.add(item)

    adj_list = {(head, tail)
                for (head, tail) in {(r[0:k], r[1:k + 1]) for r in dna_strings}
                if any(head in dna or tail in dna for dna in dna_strings)}

    superstring = []
    c = adj_list.pop()
    while adj_list:
        superstring.append(c[1][k - 1:])

        next_edge = {n for n in adj_list if n[0] == c[1]}
        if next_edge:
            c = (adj_list & next_edge).pop()
            adj_list.remove(c)
        else:
            adj_list = None

    print("".join(superstring))

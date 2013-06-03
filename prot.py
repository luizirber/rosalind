#!/usr/bin/env python

from __future__ import print_function
import os


def prepare_codon_table(filename):
    with open(filename) as data:
        codon_data = data.read().split()
    return dict(zip(codon_data[::2], codon_data[1::2]))


def protein_encoding(rna):
    codon_table = prepare_codon_table(os.path.join('data', 'codon_table'))
    output = []
    for codon in (rna[i:i + 3] for i in range(0, len(rna), 3)):
        if codon_table[codon] == 'Stop':
            break
        else:
            output.append(codon_table[codon])

    return "".join(output)


if __name__ == "__main__":
    with open(os.path.join('data', 'rosalind_prot.txt')) as dataset:
        print(protein_encoding(dataset.read().rstrip()))

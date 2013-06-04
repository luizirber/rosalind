#!/usr/bin/env python

from __future__ import print_function
import os

from Bio.Seq import translate


if __name__ == "__main__":
    with open(os.path.join('data', 'rosalind_ptra.txt')) as dataset:
        dna_string = dataset.readline().rstrip()
        protein_string = dataset.readline().rstrip()

    translation = translate(dna_string)
    print(translation.find(protein_string) + 1)

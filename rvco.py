#!/usr/bin/env python

from __future__ import print_function
import os

from Bio import SeqIO
from Bio.Alphabet import IUPAC


if __name__ == "__main__":
    with open(os.path.join('data', 'rosalind_rvco.txt')) as dataset:
        dna = list(SeqIO.parse(dataset, 'fasta', IUPAC.unambiguous_dna))

    c = 0
    for s in dna:
        if str(s.seq) == str(s.reverse_complement().seq):
            c += 1

    print(c)

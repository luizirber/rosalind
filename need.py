#!/usr/bin/env python

from __future__ import print_function
import os

from Bio.Emboss.Applications import NeedleCommandline
from Bio import SeqIO, Entrez
Entrez.email = "luiz.irber@gmail.com"


if __name__ == "__main__":
    with open(os.path.join('data', 'rosalind_need.txt')) as dataset:
        ids = dataset.read().split()

    handle = Entrez.efetch(db='nucleotide', id=ids, rettype="fasta")
    records = list(SeqIO.parse(handle, 'fasta'))

    for i, r in enumerate(records):
        with open(ids[i], 'w') as f:
            SeqIO.write(r, f, 'fasta')

    needle_cline = NeedleCommandline()
    needle_cline.asequence = ids[0]
    needle_cline.bsequence = ids[1]
    needle_cline.outfile = "need.txt"
    needle_cline.gapopen = 11
    needle_cline.gapextend = 1
    needle_cline.endopen = 11
    needle_cline.endextend = 1
    needle_cline.endweight = True

    needle_cline()

    with open('need.txt') as f:
        output = f.readlines()

    for line in output:
        if 'Score:' in line:
            print(int(float(line[:-1].split(':')[-1].strip())))

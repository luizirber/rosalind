#!/usr/bin/env python

from __future__ import print_function
import os

from Bio import SeqIO, Entrez
Entrez.email = "luiz.irber@gmail.com"


if __name__ == "__main__":
    with open(os.path.join('data', 'rosalind_frmt.txt')) as dataset:
        ids = dataset.read().rstrip().split()

        handle = Entrez.efetch(db='nucleotide', id=ids, rettype="fasta")
        records = list(SeqIO.parse(handle, 'fasta'))

        shortest = records[0]
        for r in records[1:]:
            if len(r.seq) < len(shortest.seq):
                shortest = r

        print(shortest.format('fasta'), end='')

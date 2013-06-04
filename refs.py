#!/usr/bin/env python

from __future__ import print_function
import os

from Bio import Entrez
Entrez.email = "luiz.irber@gmail.com"


if __name__ == "__main__":
    with open(os.path.join('data', 'rosalind_refs.txt')) as dataset:
        species = dataset.readline().rstrip()
        a = int(dataset.readline().rstrip())
        b = int(dataset.readline().rstrip())
        date = dataset.readline().rstrip()

    handle = Entrez.esearch(
        db='nucleotide',
        term='"%s"[Organism] AND "1900/01/01"[PDAT]:"%s"[PDAT] AND %s[SLEN]:%s[SLEN] AND srcdb_refseq[Properties]' % (species, date, a, b))

    record = Entrez.read(handle)
    print(record["Count"])

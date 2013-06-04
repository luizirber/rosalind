#!/usr/bin/env python

from __future__ import print_function
import os

from Bio import Entrez
Entrez.email = "luiz.irber@gmail.com"


if __name__ == "__main__":
    with open(os.path.join('data', 'rosalind_gbk.txt')) as dataset:
        genus = dataset.readline().rstrip()
        begin = dataset.readline().rstrip()
        end = dataset.readline().rstrip()

    handle = Entrez.esearch(
        db='nucleotide',
        term='"%s"[Organism] AND "%s"[PDAT]:"%s"[PDAT]' % (
            genus, begin, end))

    record = Entrez.read(handle)
    print(record["Count"])

#!/usr/bin/env python

from __future__ import print_function
import os

from Bio import Entrez
Entrez.email = "luiz.irber@gmail.com"


if __name__ == "__main__":
    with open(os.path.join('data', 'rosalind_pbmd.txt')) as dataset:
        author = dataset.readline().rstrip()
        year = dataset.readline().rstrip()

        handle = Entrez.esearch(
            db='pubmed',
            term='"%s"[Author] AND %s[dp]' % (author, year))
        record = Entrez.read(handle)
        print(record['IdList'][-1])

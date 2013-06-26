#!/usr/bin/env python

from __future__ import print_function, division
import os
from subprocess import call

from Bio import SeqIO


CMD = "fastq_quality_filter -Q33 -q {0} -p {1} -i {2} -o outfile"


if __name__ == "__main__":
    with open(os.path.join('data', 'rosalind_filt.txt')) as dataset:
        q, p = [int(d) for d in dataset.readline().split()]
        with open('infile', 'w') as infile:
            for line in dataset.readlines():
                infile.write(line)

    c = call(CMD.format(q, p, 'infile'), shell=True)
    with open('outfile') as outfile:
        seqs = SeqIO.parse(outfile, 'fastq')
        print(len(list(seqs)))
    os.remove('infile')
    os.remove('outfile')

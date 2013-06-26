#!/usr/bin/env python

from __future__ import print_function, division
import os

from Bio import SeqIO


if __name__ == "__main__":
    with open(os.path.join('data', 'rosalind_phre.txt')) as dataset:
        threshold = int(dataset.readline())
        data = SeqIO.parse(dataset, 'fastq')

        reads = 0
        for seq in data:
            quality = seq.letter_annotations['phred_quality']
            if sum(quality) / len(quality) <= threshold:
                reads += 1
        print(reads)

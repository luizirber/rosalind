#!/usr/bin/env python

from __future__ import print_function
import os


def rna_transcription(dna):
    return dna.replace('T', 'U')


if __name__ == "__main__":
    with open(os.path.join('data', 'rosalind_rna.txt')) as dataset:
        print(rna_transcription(dataset.read()))

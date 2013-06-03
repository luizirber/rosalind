#!/usr/bin/env python

from __future__ import print_function
import os
try:
    from string import maketrans
except ImportError:  # Python 3?
    maketrans = str.maketrans


TRANSLATION_TABLE = maketrans('ACGT', 'TGCA')


def reverse_complement(dna):
    return dna.translate(TRANSLATION_TABLE)[::-1]


if __name__ == "__main__":
    with open(os.path.join('data', 'rosalind_revc.txt')) as dataset:
        print(reverse_complement(dataset.read().rstrip()))

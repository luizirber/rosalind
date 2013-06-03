#!/usr/bin/env python

from __future__ import print_function
import os
from itertools import starmap
import operator


def hamming(s1, s2):
    return sum(starmap(operator.ne, zip(s1, s2)))


if __name__ == "__main__":
    with open(os.path.join('data', 'rosalind_hamm.txt')) as dataset:
        s, t = dataset.readlines()
        print(hamming(s.rstrip(), t.rstrip()))

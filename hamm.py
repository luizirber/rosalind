#!/usr/bin/env python

from __future__ import print_function
import os


def hamming(s1, s2):
    return sum(s1 != s2 for s1, s2 in zip(s1, s2))


if __name__ == "__main__":
    with open(os.path.join('data', 'rosalind_hamm.txt')) as dataset:
        s, t = dataset.readlines()
        print(hamming(s.rstrip(), t.rstrip()))

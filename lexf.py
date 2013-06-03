#!/usr/bin/env python

from __future__ import print_function
import os
from itertools import product


def lexf_order(size, alphabet='TAGC'):
    return [''.join(p) for p in product(alphabet, repeat=size)]


if __name__ == "__main__":
    with open(os.path.join('data', 'rosalind_lexf.txt')) as dataset:
        alphabet, size = dataset.readlines()
        print(*lexf_order(int(size), alphabet.rstrip().split()), sep='\n')

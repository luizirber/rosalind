#!/usr/bin/env python

from __future__ import print_function
import os
from itertools import product


def lexv_order(size, alphabet='TAGC'):
    output = []
    for s in range(1, size + 1):
        for p in product(alphabet, repeat=s):
            output.append(''.join(p))
    return sorted(output, key=lambda x: [alphabet.find(c) for c in x])


if __name__ == "__main__":
    with open(os.path.join('data', 'rosalind_lexv.txt')) as dataset:
        alphabet, size = [r.rstrip() for r in dataset.readlines()]
        print(*lexv_order(int(size), alphabet.replace(' ', '')), sep='\n')

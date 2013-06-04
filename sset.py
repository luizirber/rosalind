#!/usr/bin/env python

from __future__ import print_function
import os


if __name__ == "__main__":
    with open(os.path.join('data', 'rosalind_sset.txt')) as dataset:
        n = int(dataset.read().rstrip())
        print(pow(2, n, 1000000))

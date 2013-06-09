#!/usr/bin/env python

from __future__ import print_function
import os


if __name__ == "__main__":
    with open(os.path.join('data', 'rosalind_ini2.txt')) as dataset:
        a, b = [int(r) for r in dataset.readline().rstrip().split()]
        print((a ** 2) + (b ** 2))

#!/usr/bin/env python

from __future__ import print_function
import os


if __name__ == "__main__":
    with open(os.path.join('data', 'rosalind_ini4.txt')) as dataset:
        a, b = map(int, dataset.read().split())
        print(sum(i for i in range(a, b + 1) if i % 2 == 1))

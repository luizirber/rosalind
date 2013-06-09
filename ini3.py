#!/usr/bin/env python

from __future__ import print_function
import os


if __name__ == "__main__":
    with open(os.path.join('data', 'rosalind_ini3.txt')) as dataset:
        s = dataset.readline().rstrip()
        a, b, c, d = [int(r) for r in dataset.readline().rstrip().split()]
        print(s[a:b + 1], s[c:d + 1])

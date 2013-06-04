#!/usr/bin/env python

from __future__ import print_function
import os


if __name__ == "__main__":
    with open(os.path.join('data', 'rosalind_tree.txt')) as dataset:
        n = int(dataset.readline().rstrip())
        adjlist = [map(int, d.split()) for d in dataset]
        print(n - (len(adjlist) + 1))

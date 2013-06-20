#!/usr/bin/env python

from __future__ import print_function
import os

from nwck import parse_file


if __name__ == "__main__":
    with open(os.path.join('data', 'rosalind_nkew.txt')) as dataset:
        trees, nodes = parse_file(dataset)
        print(*[t.distance(*n, weighted=True)
                for t, n in zip(trees, nodes)])

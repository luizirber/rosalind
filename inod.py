#!/usr/bin/env python

from __future__ import print_function
import os


if __name__ == "__main__":
    with open(os.path.join('data', 'rosalind_inod.txt')) as dataset:
        print(int(dataset.read().rstrip()) - 2)

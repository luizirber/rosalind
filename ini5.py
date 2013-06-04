#!/usr/bin/env python

from __future__ import print_function
import os


if __name__ == "__main__":
    with open(os.path.join('data', 'rosalind_ini5.txt')) as dataset:
        DATA = dataset.readlines()
        for i, line in enumerate(DATA):
            if i % 2 == 1:
                print(line, end='')

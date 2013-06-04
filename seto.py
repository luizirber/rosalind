#!/usr/bin/env python

from __future__ import print_function
import os


def print_set(S):
    print('{' + ", ".join(str(s) for s in S) + '}')


if __name__ == "__main__":
    with open(os.path.join('data', 'rosalind_seto.txt')) as dataset:
        n = int(dataset.readline().rstrip())
        FULL = set(range(1, n + 1))
        A = set(map(int, (d for d in dataset.readline()[1:-2].split(','))))
        B = set(map(int, (d for d in dataset.readline()[1:-2].split(','))))

        print_set(A | B)
        print_set(A & B)
        print_set(A - B)
        print_set(B - A)
        print_set(FULL - A)
        print_set(FULL - B)

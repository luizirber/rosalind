#!/usr/bin/env python

from __future__ import print_function, division
import os


def partition(A):
    q = A[0]
    low = []
    high = []

    for v in A[1:]:
        if v < q:
            low.append(v)
        else:
            high.append(v)

    return low + [q] + high


if __name__ == "__main__":
    with open(os.path.join('data', 'rosalind_par.txt')) as dataset:
        dataset.readline()
        A = [int(r) for r in dataset.readline().strip().split()]

        print(*partition(A))

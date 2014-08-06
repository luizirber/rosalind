#!/usr/bin/env python

from __future__ import print_function, division
import os


def merge(A, B):
    n = len(A)
    m = len(B)
    i = j = 0
    C = []

    while i < n and j < m:
        if A[i] < B[j]:
            C.append(A[i])
            i += 1
        else:
            C.append(B[j])
            j += 1

    if i < n:
        C += A[i:]
    elif j < m:
        C += B[j:]

    return C


if __name__ == "__main__":
    with open(os.path.join('data', 'rosalind_mer.txt')) as dataset:
        dataset.readline()
        A = [int(r) for r in dataset.readline().strip().split()]
        dataset.readline()
        B = [int(r) for r in dataset.readline().strip().split()]

        print(*merge(A, B))

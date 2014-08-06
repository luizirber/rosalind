#!/usr/bin/env python

from __future__ import print_function, division
import os
import math


def binsearch(A, q):
    n = len(A)

    low_i = 0
    high_i = n - 1
    mid = math.floor(n / 2)

    prev = -1, -1, -1
    while (low_i, mid, high_i) != prev:
        prev = low_i, mid, high_i

        if q == A[low_i]:
            return low_i + 1
        elif q == A[high_i]:
            return high_i + 1
        elif q == A[mid]:
            return mid + 1
        elif q < A[mid]:
            high_i = mid
        elif q > A[mid]:
            low_i = mid

        mid = math.floor((high_i + low_i) / 2)

    return -1


if __name__ == "__main__":
    with open(os.path.join('data', 'rosalind_bins.txt')) as dataset:
        n = int(dataset.readline().strip())
        m = int(dataset.readline().strip())
        A = [int(r) for r in dataset.readline().strip().split()]
        query = [int(r) for r in dataset.readline().strip().split()]
        print(*[binsearch(A, q) for q in query])

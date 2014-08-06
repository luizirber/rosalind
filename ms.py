#!/usr/bin/env python

from __future__ import print_function, division
import os
import math


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


def merge_sort(A):
    n = len(A)

    if n == 1:
        return A

    mid = int(math.floor(n / 2))
    low = merge_sort(A[:mid])
    high = merge_sort(A[mid:])

    return merge(low, high)


if __name__ == "__main__":
    with open(os.path.join('data', 'rosalind_ms.txt')) as dataset:
        dataset.readline()
        A = [int(r) for r in dataset.readline().strip().split()]

        print(*merge_sort(A))

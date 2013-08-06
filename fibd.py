#!/usr/bin/env python

from __future__ import print_function
import os


def fibd(n, k):
    f = [0] * (n + 1)
    f[0] = 1
    for i in range(2, n + 1):
        f[i] = f[i - 2] + f[i - 1] - f[i - k - 1]

    return f[n] + f[n - 1]


if __name__ == "__main__":
    with open(os.path.join('data', 'rosalind_fibd.txt')) as dataset:
        n, k = [int(r) for r in dataset.read().split()]
    print(fibd(n, k))

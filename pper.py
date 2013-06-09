#!/usr/bin/env python

from __future__ import print_function, division
import os
from functools import reduce
import operator


def partial_permutation(n, k):
    n_fact = reduce(operator.mul, range(1, n + 1))
    n_k_fact = (reduce(operator.mul, range(1, n - k + 1)) or 1)
    return (n_fact / n_k_fact) % 1000000


if __name__ == "__main__":
    with open(os.path.join('data', 'rosalind_pper.txt')) as dataset:
        n, k = map(int, dataset.readline().rstrip().split())
        print(int(partial_permutation(n, k)))

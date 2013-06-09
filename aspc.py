#!/usr/bin/env python

from __future__ import print_function, division
import os
from math import factorial


def sum_of_combinations(n, m):
    return sum(factorial(n) // (factorial(k) * factorial(n - k))
               for k in range(m, n + 1)) % 1000000


if __name__ == "__main__":
    with open(os.path.join('data', 'rosalind_aspc.txt')) as dataset:
        n, m = [int(r) for r in dataset.readline().rstrip().split()]
    print(int(sum_of_combinations(n, m)))

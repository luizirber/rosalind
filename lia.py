#!/usr/bin/env python

from __future__ import print_function
import os
from math import factorial as fact


def ind_prob(n, k, p=.25):
    return (fact(n) / (fact(k) * fact(n - k))) * (p ** k) * (1 - p) ** (n - k)


if __name__ == "__main__":
    with open(os.path.join('data', 'rosalind_lia.txt')) as dataset:
        k, n = [int(r) for r in dataset.read().split()]

    prob = 0.0
    for i in range(n, (2 ** k) + 1):
        prob += ind_prob((2 ** k), i)
    print(round(prob, 3))

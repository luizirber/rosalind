#!/usr/bin/env python

from __future__ import print_function
import os
from itertools import permutations


def permutation(n):
    return list(permutations(range(1, n + 1), n))


if __name__ == "__main__":
    with open(os.path.join('data', 'rosalind_perm.txt')) as dataset:
        n = int(dataset.read())
        perms = permutation(n)
        print(len(perms))
        for p in perms:
            print(*p, sep=" ")

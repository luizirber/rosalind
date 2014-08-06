#!/usr/bin/env python

from __future__ import print_function, division
import os
from collections import Counter


if __name__ == "__main__":
    with open(os.path.join('data', 'rosalind_maj.txt')) as dataset:
        results = []

        n, k = [int(r) for r in dataset.readline().strip().split()]
        for line in dataset:
            A = [int(r) for r in line.strip().split()]
            c = Counter(A)
            v, occ = c.most_common()[0]
            if occ > len(A) / 2:
                results.append(v)
            else:
                results.append(-1)
        print(*results)

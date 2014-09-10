#! /usr/bin/env python

from __future__ import print_function


def skew(genome):
    total = {'G': 0, 'C': 0}
    skews = []
    for base in genome:
        skews.append(total['G'] - total['C'])
        if base in 'GC':
            total[base] += 1
    return skews


def min_skew(skews):
    min_value = None
    mins = []
    for i, v in enumerate(skews):
        if min_value is None or v < min_value:
            min_value = v
            mins = [i]
        elif v == min_value:
            mins.append(i)
    return mins

if __name__ == "__main__":
    with open('data/rosalind_1e.txt', 'r') as dataset:
        genome = dataset.readline().rstrip()
    print(*min_skew(skew(genome)))

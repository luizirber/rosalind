#!/usr/bin/env python

from __future__ import print_function
from __future__ import division
import os

from prob import prob_gc, prob_at


def prob_none_equal(N, dna, x):
    prb_gc = prob_gc(x)
    prb_at = prob_at(x)
    prob = 1  # probability that we have the same string
    for base in dna:
        if base in ('A', 'T'):
            prob *= prb_at
        else:
            prob *= prb_gc
    return (1 - prob) ** N


if __name__ == "__main__":
    with open(os.path.join('data', 'rosalind_rstr.txt')) as dataset:
        N, x = dataset.readline().rstrip().split()
        dna = dataset.readline().rstrip()
    print(round(1 - prob_none_equal(int(N), dna, float(x)), 3))

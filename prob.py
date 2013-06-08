#!/usr/bin/env python

from __future__ import print_function
from __future__ import division
import os
from functools import reduce
import operator
import math


def prob_gc(gc_cont):
    return gc_cont / 2


def prob_at(gc_cont):
    return (1 - gc_cont) / 2


if __name__ == "__main__":
    with open(os.path.join('data', 'rosalind_prob.txt')) as dataset:
        dna = dataset.readline().rstrip().upper()
        gc_contents = list(map(float, dataset.readline().rstrip().split()))

    output = []
    for gc_cont in gc_contents:
        gc = prob_gc(gc_cont)
        at = prob_at(gc_cont)
        probs = [(at if s in ('A', 'T') else gc) for s in dna]
        output.append(round(math.log10(reduce(operator.mul, probs)), 3))
    print(*output)

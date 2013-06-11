#!/usr/bin/env python

from __future__ import print_function
import os
from collections import Counter
import operator


def mink_oper(set1, set2, oper=operator.add):
    return [round(oper(s1, s2), 5) for s1 in set1 for s2 in set2]


def mink_sum(set1, set2):
    return mink_oper(set1, set2)


def mink_diff(set1, set2):
    return [abs(r) for r in mink_oper(set1, set2, oper=operator.sub)]


def multiplicity(s1, s2):
    diff = mink_diff(s1, s2)
    multiplicity = Counter(diff)
    return multiplicity.most_common()[0][::-1]


if __name__ == "__main__":
    with open(os.path.join('data', 'rosalind_conv.txt')) as dataset:
        s1 = [round(float(r), 5) for r in dataset.readline().rstrip().split()]
        s2 = [round(float(r), 5) for r in dataset.readline().rstrip().split()]

    print(*multiplicity(s1, s2), sep='\n')

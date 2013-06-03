#!/usr/bin/env python

from __future__ import print_function
import os


def substring_find(s1, s2):
    pos = s1.find(s2)
    while pos >= 0:
        yield pos + 1
        pos = s1.find(s2, pos + 1)


if __name__ == "__main__":
    with open(os.path.join('data', 'rosalind_subs.txt')) as dataset:
        s, t = dataset.readlines()
        print(*list(substring_find(s.rstrip(), t.rstrip())))

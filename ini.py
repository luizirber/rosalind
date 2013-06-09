#!/usr/bin/env python

from __future__ import print_function
import os

from Bio.Seq import Seq


if __name__ == "__main__":
    with open(os.path.join('data', 'rosalind_ini.txt')) as dataset:
        seq = Seq(dataset.read().rstrip())
        print(*[seq.count(a) for a in ('A', 'C', 'G', 'T')])

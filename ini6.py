#!/usr/bin/env python

from __future__ import print_function
import os
from collections import Counter


if __name__ == "__main__":
    with open(os.path.join('data', 'rosalind_ini6.txt')) as dataset:
        DATA = dataset.readline()
    c = Counter(DATA.split())
    for freq in c.most_common():
        print(*freq)

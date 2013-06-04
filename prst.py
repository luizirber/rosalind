#!/usr/bin/env python

from __future__ import print_function
import os

from Bio.ExPASy import ScanProsite


if __name__ == "__main__":
    with open(os.path.join('data', 'rosalind_prst.txt')) as dataset:
        protein_string = dataset.readline().rstrip()

    handle = ScanProsite.scan(protein_string)
    result = ScanProsite.read(handle)

    print(sorted(result, key=lambda x: x['start'])[-1]['signature_ac'])

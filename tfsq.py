#!/usr/bin/env python

from __future__ import print_function
import os
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

from Bio import SeqIO


if __name__ == "__main__":
    with open(os.path.join('data', 'rosalind_tfsq.txt')) as dataset:
        handle = StringIO("")
        SeqIO.convert(dataset, 'fastq', handle, "fasta")
        print(handle.getvalue())

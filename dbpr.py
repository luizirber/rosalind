#!/usr/bin/env python

from __future__ import print_function
import os

from Bio import ExPASy


if __name__ == "__main__":
    with open(os.path.join('data', 'rosalind_dbpr.txt')) as dataset:
        uniprot_id = dataset.readline().rstrip()

    processes = []
    handle = ExPASy.get_sprot_raw(uniprot_id)
    for line in [l.decode('utf-8') for l in handle.readlines()]:
        if (line.startswith('DR') and
           ('GO;' in line) and
           ('P:' in line)):
            processes.append(line[:-1])

    for proc in processes:
        print(proc.split(';')[2].split(':')[1])

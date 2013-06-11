#!/usr/bin/env python

from __future__ import print_function
import os

try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen

from revp import read_fasta
from subs import substring_find


UNIPROT_URL = 'http://www.uniprot.org/uniprot/'


def find_N_glycosylation_motif(protein):
    finds = []
    for pos in substring_find(protein, 'N'):
        if len(protein[pos-1:pos + 3]) == 4:
            if (protein[pos] != 'P' and protein[pos + 1] in ('S', 'T')
                and protein[pos + 2] != 'P'):
                    finds.append(pos)
    return finds


if __name__ == "__main__":
    with open(os.path.join('data', 'rosalind_mprt.txt')) as dataset:
        uniprot_ids = [r.rstrip() for r in dataset.readlines()]

    proteins = {}
    for uniprot_id in uniprot_ids:
        prot = urlopen('{0}{1}.fasta'.format(UNIPROT_URL, uniprot_id))
        proteins[uniprot_id] = read_fasta(prot).popitem()[1]
        prot.close()

    for protein in proteins:
        pos = find_N_glycosylation_motif(proteins[protein])
        if pos:
            print(protein)
            print(*pos)

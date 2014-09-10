#!/usr/bin/env python

from __future__ import print_function
import os

from Bio.Seq import Seq, translate
from Bio.Alphabet import IUPAC


if __name__ == "__main__":
    with open(os.path.join('data', 'rosalind_orfr.txt')) as dataset:
        dna_string = Seq(dataset.read().rstrip(), IUPAC.unambiguous_dna)

    dna_strings = [dna_string, dna_string.reverse_complement()]

    longest = None
    for i in range(3):
        for dna in dna_strings:
            trans = translate(dna[i:], to_stop=True)
            if not longest or len(longest) < len(trans):
                longest = trans

    print(longest)

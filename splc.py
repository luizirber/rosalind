#!/usr/bin/env python

from __future__ import print_function
import os

from revp import read_fasta
from prot import protein_encoding
from rna import rna_transcription


def rna_splicing(dna, introns):
    for intron in introns:
        dna = dna.replace(introns[intron], '')
    rna_string = rna_transcription(dna)
    return protein_encoding(rna_string)


if __name__ == "__main__":
    with open(os.path.join('data', 'rosalind_splc.txt')) as dataset:
        seqs = read_fasta(dataset)
        dna = seqs.popitem(last=False)
        print(rna_splicing(dna[1], seqs))

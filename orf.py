#!/usr/bin/env python

from __future__ import print_function
import os

from prot import prepare_codon_table
from revp import read_fasta
from revc import reverse_complement
from rna import rna_transcription
from subs import substring_find


if __name__ == "__main__":
    with open(os.path.join('data', 'rosalind_orf.txt')) as dataset:
        seqs = read_fasta(dataset)

    codon_table = prepare_codon_table(os.path.join('data', 'codon_table'))

    output = []
    dna = seqs.popitem()[1]
    rna = (rna_transcription(dna), rna_transcription(reverse_complement(dna)))

    for seq in rna:
        for offset in (0, 1, 2):
            for start_pos in substring_find(seq[offset:], 'AUG'):
                current = []
                for codon in (seq[i:i+3] for i in range(start_pos, len(seq), 3)):
                    if len(codon) == 3:
                        if codon_table[codon] == 'Stop' and current:
                            output.append(''.join(current))
                            current = []
                        elif codon == 'AUG' or current:
                            current.append(codon_table[codon])

    print("\n".join(set(output)))

import os

from Bio import SeqIO
from Bio.Alphabet import IUPAC


PROJPATH = os.path.abspath(os.path.join(
    os.path.dirname(__file__), os.path.pardir))


with open(os.path.join(PROJPATH, 'data', 'rosalind_rvco.txt')) as f:
    dna_strings = list(SeqIO.parse(f, 'fasta', IUPAC.unambiguous_dna))

c = 0
for s in dna_strings:
    if str(s.seq) == str(s.reverse_complement().seq):
        c += 1

print c

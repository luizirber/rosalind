import os

from Bio.Seq import translate


PROJPATH = os.path.abspath(os.path.join(
    os.path.dirname(__file__), os.path.pardir))


with open(os.path.join(PROJPATH, 'data', 'rosalind_ptra.txt')) as f:
    DATA = f.readlines()

dna_string = DATA[0][:-1]
protein_string = DATA[1][:-1]

translation = translate(dna_string)
print translation.find(protein_string) + 1

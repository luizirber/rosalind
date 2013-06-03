import os
import operator

PROJPATH = os.path.abspath(os.path.join(
    os.path.dirname(__file__), os.path.pardir))
TABLE = open('codon_table').read()
codon_data = TABLE.split()
codon_table = dict(zip(codon_data[::2], codon_data[1::2]))

with open(os.path.join(PROJPATH, 'data', 'rosalind_mrna.txt')) as f:
    protein_string = f.read()[:-1]

stop_codons = [c for c in codon_table if codon_table[c] == 'Stop']

possibilities = []
for p in protein_string:
    possibilities.append([(p, c) for c in codon_table if codon_table[c] == p])

print ((len(stop_codons) * reduce(operator.mul, map(len, possibilities))) % 1000000)

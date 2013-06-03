import os
from string import maketrans


PROJPATH = os.path.abspath(os.path.join(
    os.path.dirname(__file__), os.path.pardir))
TRANSLATION_TABLE = maketrans('ACGT', 'TGCA')


with open(os.path.join(PROJPATH, 'data', 'rosalind_dbru.txt')) as f:
    DATA = f.readlines()

dna_set = set(s[:-1] for s in DATA)
reverse_complements = {s.translate(TRANSLATION_TABLE)[::-1] for s in dna_set}
dna_strings = dna_set | reverse_complements

k = len(DATA[0][:-1]) - 1
adj_list = {(r[0:k], r[1:k+1]) for r in dna_strings}

for adj in sorted(adj_list):
    print '(' + adj[0] + ', ' + adj[1] + ')'

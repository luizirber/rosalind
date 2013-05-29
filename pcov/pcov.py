import os
from string import maketrans


PROJPATH = os.path.abspath(os.path.join(
    os.path.dirname(__file__), os.path.pardir))
TRANSLATION_TABLE = maketrans('ACGT', 'TGCA')


with open(os.path.join(PROJPATH, 'data', 'rosalind_pcov.txt')) as f:
    DATA = f.readlines()

reads = {s[:-1] for s in DATA}
reverse_complements = {s[::-1].translate(TRANSLATION_TABLE) for s in reads}
dna_strings = reads | reverse_complements

k = len(DATA[0][:-1]) - 1
adj_list = {(head, tail)
            for (head, tail) in {(r[0:k], r[1:k + 1]) for r in dna_strings}
            if any(head in dna or tail in dna for dna in dna_strings)}

superstring = []
c = adj_list.pop()
while adj_list:
    superstring.append(c[1][k - 1:])

    next_edge = {n for n in adj_list if n[0] == c[1]}
    if next_edge:
        c = (adj_list & next_edge).pop()
        adj_list.remove(c)
    else:
        adj_list = None

print "".join(superstring)

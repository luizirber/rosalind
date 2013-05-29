import os
from string import maketrans


PROJPATH = os.path.abspath(os.path.join(
    os.path.dirname(__file__), os.path.pardir))
TRANSLATION_TABLE = maketrans('ACGT', 'TGCA')


with open(os.path.join(PROJPATH, 'data', 'rosalind_pcov.txt')) as f:
    DATA = f.readlines()

dna_set = set(s[:-1] for s in DATA)
reverse_complements = {s[::-1].translate(TRANSLATION_TABLE) for s in dna_set}
dna_strings = dna_set | reverse_complements

k = len(DATA[0][:-1]) - 1
adj_list = {(r[0:k], r[1:k+1]) for r in dna_strings}

candidates = set()
for dna in dna_set:
    for adj in sorted(adj_list):
        if adj[0] in dna or adj[1] in dna:
            candidates.add(adj)

superstring = []
c = candidates.pop()
while candidates:
    if not superstring:
        superstring.append(c[0][k-1:])
    superstring.append(c[1][k-1:])

    adj = {n for n in candidates if n[0] == c[1]}
    if adj:
        c = (candidates & adj).pop()
        candidates.remove(c)
    else:
        candidates = None

print "".join(superstring)

import os

from Bio import Entrez
Entrez.email = "luiz.irber@gmail.com"


PROJPATH = os.path.abspath(os.path.join(
    os.path.dirname(__file__), os.path.pardir))

with open(os.path.join(PROJPATH, 'data', 'rosalind_refs.txt')) as f:
    DATA = f.readlines()

species = DATA[0][:-1]
a = int(DATA[1][:-1])
b = int(DATA[2][:-1])
date = DATA[3][:-1]

handle = Entrez.esearch(
            db='nucleotide',
            term='"%s"[Organism] AND "1900/01/01"[PDAT]:"%s"[PDAT] AND %s[SLEN]:%s[SLEN] AND srcdb_refseq[Properties]' % (species, date, a, b))

record = Entrez.read(handle)
print record["Count"]

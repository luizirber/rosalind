import os

from Bio import Entrez
Entrez.email = "luiz.irber@gmail.com"


PROJPATH = os.path.abspath(os.path.join(
    os.path.dirname(__file__), os.path.pardir))

with open(os.path.join(PROJPATH, 'data', 'rosalind_gbk.txt')) as f:
    DATA = f.readlines()

genus = DATA[0][:-1]
begin = DATA[1][:-1]
end = DATA[2][:-1]

handle = Entrez.esearch(
            db='nucleotide',
            term='"%s"[Organism] AND "%s"[PDAT]:"%s"[PDAT]' % (genus, begin, end))

record = Entrez.read(handle)
print record["Count"]

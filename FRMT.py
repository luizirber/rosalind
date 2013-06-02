import os

from Bio import SeqIO, Entrez
Entrez.email = "luiz.irber@gmail.com"


PROJPATH = os.path.abspath(os.path.join(
    os.path.dirname(__file__), os.path.pardir))

with open(os.path.join(PROJPATH, 'data', 'rosalind_frmt.txt')) as f:
    DATA = f.read()

ids = DATA.split()

handle = Entrez.efetch(db='nucleotide', id=ids, rettype="fasta")
records = list(SeqIO.parse(handle, 'fasta'))

shortest = records[0]
for r in records[1:]:
    if len(r.seq) < len(shortest.seq):
        shortest = r

print shortest.format('fasta'),

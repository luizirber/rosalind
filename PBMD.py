import os

from Bio import Entrez
Entrez.email = "luiz.irber@gmail.com"


PROJPATH = os.path.abspath(os.path.join(
    os.path.dirname(__file__), os.path.pardir))

with open(os.path.join(PROJPATH, 'data', 'rosalind_pbmd.txt')) as f:
    DATA = f.readlines()

author = DATA[0][:-1]
year = DATA[1][:-1]

handle = Entrez.esearch(db='pubmed', term='"%s"[Author] AND %s[dp]' % (author, year))
record = Entrez.read(handle)
print record['IdList'][-1]

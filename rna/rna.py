import os

PROJPATH = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))

SAMPLE = open(os.path.join(PROJPATH, 'data', 'rosalind_rna.txt')).read()

print SAMPLE.replace('T', 'U')

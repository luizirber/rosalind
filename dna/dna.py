import os

PROJPATH = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))

SAMPLE = open(os.path.join(PROJPATH, 'data', 'rosalind_dna.txt')).read()

print map(SAMPLE.count, ["A", "C", "G", "T"])

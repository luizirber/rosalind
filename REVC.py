from string import maketrans
import os

PROJPATH = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))

SAMPLE = open(os.path.join(PROJPATH, 'data', 'rosalind_revc.txt')).read()

print SAMPLE.translate(maketrans('ACGT', 'TGCA'))[::-1]

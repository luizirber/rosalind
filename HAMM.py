from itertools import starmap, izip
import operator
import os

PROJPATH = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))

SAMPLES = open(os.path.join(PROJPATH, 'data', 'rosalind_hamm.txt')).readlines()

def hamming(s1, s2):
    return sum(starmap(operator.ne, izip(s1, s2)))

print hamming(SAMPLES[0], SAMPLES[1])

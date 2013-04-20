from itertools import product
import os

PROJPATH = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))

SAMPLES = open(os.path.join(PROJPATH, 'data', 'rosalind_lexf.txt')).readlines()

alphabet = SAMPLES[0][:-1].split()
n = int(SAMPLES[1][:-1])

output = []
for p in product(alphabet, repeat=n):
    for i in p:
        output.append(i)
    output.append('\n')

print "".join(output[:-1])

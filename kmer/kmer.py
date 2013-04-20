from itertools import product
import os
from collections import OrderedDict


def read_fasta(filename):
    seqs = OrderedDict()
    with open(filename) as fp:
        current = None
        buff = []
        for line in fp:
            if line.startswith('>'):
                if current:
                    seqs[current] = ''.join(buff).strip()
                    buff = []
                current = line[:-1]
            else:
                buff.append(line[:-1])
        seqs[current] = ''.join(buff).strip()
    return seqs


def substring_count(s1, s2):
    pos = s1.find(s2)
    while pos >= 0:
        yield pos + 1
        pos = s1.find(s2, pos + 1)


PROJPATH = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
seqs = read_fasta(os.path.join(PROJPATH, 'data', 'rosalind_kmer.txt'))
dna_string = seqs[seqs.keys()[0]]

alphabet = 'A C G T'.split()

output = []
for p in product(alphabet, repeat=4):
    pos = list(substring_count(dna_string, ''.join(p)))
    output.append(str(len(pos)))

print " ".join(output)

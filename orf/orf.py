import os
from collections import OrderedDict
from string import maketrans


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


def substring_find(s1, s2):
    pos = s1.find(s2)
    while pos >= 0:
        yield pos + 1
        pos = s1.find(s2, pos + 1)


PROJPATH = os.path.abspath(os.path.join(
    os.path.dirname(__file__), os.path.pardir))
TRANSLATION_TABLE = maketrans('ACGT', 'TGCA')

TABLE = open('codon_table').read()
SAMPLES = read_fasta(os.path.join(PROJPATH, 'data', 'rosalind_orf.txt'))

codon_data = TABLE.split()
codon_table = dict(zip(codon_data[::2], codon_data[1::2]))

output = []
dna = SAMPLES[SAMPLES.keys()[0]]
rna = (dna.replace('T', 'U'),
       dna.translate(TRANSLATION_TABLE)[::-1].replace('T', 'U'))

for SAMPLE in rna:
    for offset in (0, 1, 2):
        for start_pos in substring_find(SAMPLE[offset:], 'AUG'):
            current = []
            for codon in (SAMPLE[i:i+3] for i in xrange(start_pos, len(SAMPLE), 3)):
                if len(codon) == 3:
                    if codon_table[codon] == 'Stop' and current:
                        output.append(''.join(current))
                        current = []
                    elif codon == 'AUG' or current:
                        current.append(codon_table[codon])

print "\n".join(set(output))

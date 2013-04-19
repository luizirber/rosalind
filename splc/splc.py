import os
from collections import OrderedDict

PROJPATH = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
TABLE = open('codon_table').read()
codon_data = TABLE.split()
codon_table = dict(zip(codon_data[::2], codon_data[1::2]))

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

seqs = read_fasta(os.path.join(PROJPATH, 'data', 'rosalind_splc.txt'))
dna_string = seqs[seqs.keys()[0]]

for intron in seqs.keys()[1:]:
    dna_string = dna_string.replace(seqs[intron], '')

dna_string = dna_string.replace('T', 'U')

output = []
for codon in (dna_string[i:i+3] for i in xrange(0, len(dna_string), 3)):
    if codon_table[codon] == 'Stop':
        break
    else:
        output.append(codon_table[codon])

print "".join(output)

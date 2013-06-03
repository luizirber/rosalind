from string import maketrans
import os

PROJPATH = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))

TABLE = open('codon_table').read()
SAMPLE = open(os.path.join(PROJPATH, 'data', 'rosalind_prot.txt')).read()[:-1]

codon_data = TABLE.split()
codon_table = dict(zip(codon_data[::2], codon_data[1::2]))

output = []
for codon in (SAMPLE[i:i+3] for i in xrange(0, len(SAMPLE), 3)):
    if codon_table[codon] == 'Stop':
        break
    else:
        output.append(codon_table[codon])

print "".join(output)

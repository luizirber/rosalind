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


PROJPATH = os.path.abspath(os.path.join(
    os.path.dirname(__file__), os.path.pardir))
seqs = read_fasta(os.path.join(PROJPATH, 'data', 'rosalind_grph.txt'))

output = []
for seq in seqs:
    seq_end = seqs[seq][-3:]
    adjs = seqs.keys()
    adjs.remove(seq)
    for adj in adjs:
        if seq_end == seqs[adj][:3]:
            output.append("%s %s" % (seq[1:], adj[1:]))

print "\n".join(output)

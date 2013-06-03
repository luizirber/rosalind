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


PROJPATH = os.path.abspath(os.path.join(
    os.path.dirname(__file__), os.path.pardir))
seqs = read_fasta(os.path.join(PROJPATH, 'data', 'rosalind_long.txt'))

superstring = []
vertex = set()
for seq in seqs:
    seq_data = seqs[seq]
    overlap_seq = len(seq_data) / 2

    adjs = seqs.keys()
    adjs.remove(seq)
    for adj in adjs:
        overlap = overlap_seq
        adj_data = seqs[adj]
        overlap_adj = len(adj_data) / 2

        if overlap < overlap_adj:
            overlap = overlap_adj

        pos = list(substring_count(seq_data, adj_data[:overlap]))
        if pos:
            vertex.add((seq, adj, pos[-1]))

for v in vertex:
    if not superstring:
        superstring.append((v[0], v[2]))
        superstring.append((v[1], None))

    remainder = vertex - set([v])
    for r in remainder:
        if r[0] == superstring[-1][0]:
            superstring[-1] = (r[0], r[2])
            superstring.append((r[1], None))
        elif r[1] == superstring[0][0]:
            superstring.insert(0, (r[0], r[2]))

output = []
for k, pos in reversed(superstring):
    if pos:
        output.insert(0, seqs[k][:pos-1])
    else:
        output.append(seqs[k])

print "".join(output)

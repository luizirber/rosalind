import os

PROJPATH = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))

def gc_content(seq):
    count = seq.count('C') + seq.count('G')
    return float(count) / len(seq)

def read_fasta(filename):
    seqs = {}
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

seqs = read_fasta(os.path.join(PROJPATH, 'data', 'rosalind_gc.txt'))
maxes = max(map(gc_content, seqs.values()), seqs.keys())

print maxes[0][1:], "%.6f%%" % (gc_content(seqs[maxes[0]]) * 100)

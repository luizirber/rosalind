import os
import itertools

PROJPATH = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))

SAMPLES = open(os.path.join(PROJPATH, 'data', 'rosalind_cons.txt')).read().strip('\n').split()

def prof_matrix(strings):
    profs = dict.fromkeys('A C G T'.split(), None)
    size = len(strings[0])
    for s in strings:
        for i, c in enumerate(s):
            if not profs[c]:
                profs[c] = { i:0 for i in xrange(size) }
            profs[c][i] = profs[c].get(i, 0) + 1
    return profs

def print_prof_matrix(pmat):
    for c in sorted(pmat):
        print "%s: %s" % (c, " ".join([str(v) for k, v in sorted(pmat[c].items())]))

def consensus(pmatrix):
    maxs = []
    for i in range(len(pmatrix['A'])):
        m = 0
        for k in pmatrix:
            if pmat[k][i] > m:
                m = pmat[k][i]
                mk = k
        maxs.append(mk)
    return "".join(maxs)

pmat = prof_matrix(SAMPLES)
print consensus(pmat)
print_prof_matrix(pmat)

from itertools import permutations
import os

PROJPATH = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))

SAMPLES = open(os.path.join(PROJPATH, 'data', 'rosalind_perm.txt')).readlines()

n = int(SAMPLES[0][:-1])

perms = list(permutations(range(1, n + 1), n))
print len(perms)
for p in perms:
    for i in p:
        print i,
    print

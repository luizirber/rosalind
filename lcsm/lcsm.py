import os

PROJPATH = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))

SAMPLES = open(os.path.join(PROJPATH, 'data', 'rosalind_lcsm.txt')).read().strip('\n').split()

def lcs(s1, s2):
    L = {}
    z = 0

    for i, c1 in enumerate(s1):
        for j, c2 in enumerate(s2):
            if c1 == c2:
                L[(i, j)] = L.get((i-1, j-1), 0) + 1

                if L[(i, j)] > z:
                    z = L[(i, j)]
                    ret = s1[i-z+1:i+1]
    return ret

print reduce(lcs, SAMPLES)

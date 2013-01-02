import os

PROJPATH = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))

SAMPLES = open(os.path.join(PROJPATH, 'data', 'rosalind_subs.txt')).readlines()

def substring_count(s1, s2):
    pos = s1.find(s2)
    while pos >= 0:
        yield pos + 1
        pos = s1.find(s2, pos + 1)

print list(substring_count(SAMPLES[0][:-1], SAMPLES[1][:-1]))

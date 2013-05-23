import os


PROJPATH = os.path.abspath(os.path.join(
    os.path.dirname(__file__), os.path.pardir))

with open(os.path.join(PROJPATH, 'data', 'rosalind_ini5.txt')) as f:
    DATA = f.readlines()

for i, line in enumerate(DATA):
    if i % 2 == 1:
        print line,

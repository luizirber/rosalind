import os


PROJPATH = os.path.abspath(
    os.path.join(os.path.dirname(__file__), os.path.pardir))

DATA = open(os.path.join(PROJPATH, 'data', 'rosalind_sset.txt')).read()
n = int(DATA[:-1])

print pow(2, n, 1000000)

import os


PROJPATH = os.path.abspath(os.path.join(
    os.path.dirname(__file__), os.path.pardir))

with open(os.path.join(PROJPATH, 'data', 'rosalind_ini4.txt')) as f:
    DATA = f.read()

a, b = map(int, DATA.split())

print sum(i for i in range(a, b + 1) if i % 2 == 1)

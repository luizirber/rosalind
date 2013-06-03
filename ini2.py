import os


PROJPATH = os.path.abspath(os.path.join(
    os.path.dirname(__file__), os.path.pardir))

with open(os.path.join(PROJPATH, 'data', 'rosalind_ini2.txt')) as f:
    DATA = f.read()

a, b = map(int, DATA.split())

print (a ** 2) + (b ** 2)

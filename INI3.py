import os


PROJPATH = os.path.abspath(os.path.join(
    os.path.dirname(__file__), os.path.pardir))

with open(os.path.join(PROJPATH, 'data', 'rosalind_ini3.txt')) as f:
    DATA = f.readlines()

s = DATA[0][:-1]
a, b, c, d = map(int, DATA[1].split())

print s[a:b + 1], s[c:d + 1]

import os


PROJPATH = os.path.abspath(os.path.join(
    os.path.dirname(__file__), os.path.pardir))

with open(os.path.join(PROJPATH, 'data', 'rosalind_tree.txt')) as f:
    DATA = f.readlines()

n = int(DATA[0][:-1])
adjlist = [map(int, d.split()) for d in DATA[1:]]

print n - (len(adjlist) + 1)

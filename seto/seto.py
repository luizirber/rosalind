import os


def print_set(S):
    print '{' + ", ".join(str(s) for s in S) + '}'

PROJPATH = os.path.abspath(os.path.join(
    os.path.dirname(__file__), os.path.pardir))

with open(os.path.join(PROJPATH, 'data', 'rosalind_seto.txt')) as f:
    DATA = f.readlines()

n = int(DATA[0][:-1])
FULL = set(range(1, n + 1))
A = set(map(int, (d for d in DATA[1][1:-2].split(','))))
B = set(map(int, (d for d in DATA[2][1:-2].split(','))))


print_set(A | B)
print_set(A & B)
print_set(A - B)
print_set(B - A)
print_set(FULL - A)
print_set(FULL - B)

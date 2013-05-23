import os

from Bio.ExPASy import ScanProsite


PROJPATH = os.path.abspath(os.path.join(
    os.path.dirname(__file__), os.path.pardir))

with open(os.path.join(PROJPATH, 'data', 'rosalind_prst.txt')) as f:
    DATA = f.read()

protein_string = DATA[:-1]

handle = ScanProsite.scan(protein_string)
result = ScanProsite.read(handle)

print sorted(result, key=lambda x: x['start'])[-1]['signature_ac']

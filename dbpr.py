import os

from Bio import ExPASy


PROJPATH = os.path.abspath(os.path.join(
    os.path.dirname(__file__), os.path.pardir))

with open(os.path.join(PROJPATH, 'data', 'rosalind_dbpr.txt')) as f:
    DATA = f.read()

uniprot_id = DATA[:-1]

processes = []
handle = ExPASy.get_sprot_raw(uniprot_id)
for line in handle.readlines():
    if (line.startswith('DR') and
      ('GO;' in line) and
      ('P:' in line)):
        processes.append(line[:-1])

for proc in processes:
    print proc.split(';')[2].split(':')[1]

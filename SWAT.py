import os

from Bio.Emboss.Applications import WaterCommandline
from Bio import ExPASy
from Bio import SeqIO


PROJPATH = os.path.abspath(os.path.join(
    os.path.dirname(__file__), os.path.pardir))

with open(os.path.join(PROJPATH, 'data', 'rosalind_swat.txt')) as f:
    ids = f.read().split()

for i in ids:
    handle = ExPASy.get_sprot_raw(i)
    r = SeqIO.read(handle, "swiss")
    handle.close()
    with open(i, 'w') as f:
        SeqIO.write(r, f, 'fasta')

water_cline = WaterCommandline()
water_cline.asequence = ids[0]
water_cline.bsequence = ids[1]
water_cline.outfile = "water.txt"
water_cline.gapopen = 10
water_cline.gapextend = 1

water_cline()

with open('water.txt') as f:
    output = f.readlines()

for line in output:
    if 'Score:' in line:
        print int(float(line[:-1].split(':')[-1].strip()))

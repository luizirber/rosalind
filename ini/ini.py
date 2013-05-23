import os

from Bio.Seq import Seq


PROJPATH = os.path.abspath(os.path.join(
    os.path.dirname(__file__), os.path.pardir))

with open(os.path.join(PROJPATH, 'data', 'rosalind_ini.txt')) as f:
    DATA = f.read()

seq = Seq(DATA[:-1])
print seq.count('A'), seq.count('C'), seq.count('G'), seq.count('T')

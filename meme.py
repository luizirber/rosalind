#!/usr/bin/env python

from __future__ import print_function, division
import os
from subprocess import call


CMD = "meme-meme.bin data/rosalind_meme.txt -text -nostatus -protein -minw 20 > outfile"


if __name__ == "__main__":
    c = call(CMD, shell=True)

    with open('outfile') as outfile:
        for line in outfile:
            if 'regular expression' in line:
                sep = outfile.readline()
                regex = outfile.readline().rstrip()
                break

    os.remove('outfile')
    print(regex)

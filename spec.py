#!/usr/bin/env python

from __future__ import print_function
import os

from prtm import prepare_mass_table


def protein_from_spectrum(spectrum):
    mass_table = prepare_mass_table(os.path.join('data', 'monoisotopic_mass'))
    masses = {round(mass_table[m], 2): m for m in mass_table}
    diff = [round(m2 - m1, 2) for (m1, m2) in zip(spectrum[:-1], spectrum[1:])]
    return [masses[d] for d in diff]


if __name__ == "__main__":
    with open(os.path.join('data', 'rosalind_spec.txt')) as dataset:
        prefix_spectrum = [float(r.rstrip()) for r in dataset.readlines()]
        print(*protein_from_spectrum(prefix_spectrum), sep='')

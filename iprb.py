#!/usr/bin/env python

from __future__ import print_function
import os


def prob_table():
    p = {}
    p['k|kk'] = 1
    p['m|kk'] = 0
    p['n|kk'] = 0

    p['k|km'] = .5
    p['m|km'] = .5
    p['n|km'] = 0

    p['k|mm'] = .25
    p['m|mm'] = .5
    p['n|mm'] = .25

    p['k|mn'] = 0
    p['m|mn'] = .5
    p['n|mn'] = .5

    p['k|nn'] = 0
    p['m|nn'] = 0
    p['n|nn'] = 1

    p['k|kn'] = 0
    p['m|kn'] = 1
    p['n|kn'] = 0

    return p


def prob(k, m, n):
    population = float(k + m + n)
    p = prob_table()
    p['k'] = k / population
    p['m'] = m / population
    p['n'] = n / population

    p['kk'] = k / population * (k - 1) / (population - 1)
    p['km'] = k / population * m / (population - 1) * 2
    p['mm'] = m / population * (m - 1) / (population - 1)
    p['mn'] = m / population * n / (population - 1) * 2
    p['nn'] = n / population * (n - 1) / (population - 1)
    p['kn'] = k / population * n / (population - 1) * 2

    pk = ((p['kk']) * (p['k|kk'] + p['m|kk']) +
          (p['km']) * (p['k|km'] + p['m|km']) +
          (p['mm']) * (p['k|mm'] + p['m|mm']) +
          (p['mn']) * (p['k|mn'] + p['m|mn']) +
          (p['nn']) * (p['k|nn'] + p['m|nn']) +
          (p['kn']) * (p['k|kn'] + p['m|kn']))
    return pk


if __name__ == "__main__":
    with open(os.path.join('data', 'rosalind_iprb.txt')) as dataset:
        k, m, n = [int(r) for r in dataset.read().split()]

        print(prob(k, m, n))

#!/usr/bin/env python

from __future__ import print_function, division
import os

from iprb import prob_table


def expv(kk, km, kn, mm, mn, nn):
    population = sum([kk, km, kn, mm, mn, nn])
    p = prob_table()

    pk = ((p['k|kk'] + p['m|kk']) * kk / population +
          (p['k|km'] + p['m|km']) * km / population +
          (p['k|mm'] + p['m|mm']) * mm / population +
          (p['k|mn'] + p['m|mn']) * mn / population +
          (p['k|kn'] + p['m|kn']) * kn / population)
    return round(pk * (population * 2), 3)


if __name__ == "__main__":
    with open(os.path.join('data', 'rosalind_iev.txt')) as dataset:
        n_couples = [int(r) for r in dataset.readline().rstrip().split()]
    print(expv(*n_couples))

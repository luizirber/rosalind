#!/usr/bin/env python

from __future__ import print_function, division
import os


def insertions(a):
    ins = 0
    for i in range(1, len(a)):
        k = i
        while k > 0 and a[k] < a[k - 1]:
            a[k - 1], a[k] = a[k], a[k - 1]
            k = k - 1
            ins += 1
    return ins


if __name__ == "__main__":
    with open(os.path.join('data', 'rosalind_ins.txt')) as dataset:
        n = int(dataset.readline().strip())
        A = [int(r) for r in dataset.readline().strip().split()]

        print(insertions(A))

#! /usr/bin/env python

from __future__ import print_function


TRANS_TABLE = ''.maketrans('ACGT', 'TGCA')


def reverse(text):
    return text.translate(TRANS_TABLE)[::-1]


if __name__ == "__main__":
    with open('data/rosalind_1b.txt', 'r') as dataset:
        text = dataset.readline().rstrip()
    print(reverse(text))

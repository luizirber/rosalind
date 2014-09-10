#! /usr/bin/env python

from __future__ import print_function


def kdiff(pattern, kmer):
    return sum(1 for (a, b) in zip(pattern, kmer) if a != b)


def ap_frequent(pattern, text, d):
    k = len(pattern)
    pos = []
    for i in range(len(text) - k + 1):
        kmer = text[i:i + k]
        if kdiff(pattern, kmer) <= d:
            pos.append(i)
    return pos


if __name__ == "__main__":
    with open('data/rosalind_1f.txt', 'r') as dataset:
        pattern = dataset.readline().rstrip()
        text = dataset.readline().rstrip()
        d = int(dataset.readline().rstrip())
    freq = ap_frequent(pattern, text, d)
    print(*freq)

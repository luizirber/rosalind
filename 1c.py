#! /usr/bin/env python

from __future__ import print_function


def match(pattern, genome):
    pos = []
    for i, c in enumerate(genome[:-len(pattern)]):
        if genome[i:i + len(pattern)] == pattern:
            pos.append(i)

    return pos


if __name__ == "__main__":
    with open('data/rosalind_1c.txt', 'r') as dataset:
        pattern = dataset.readline().rstrip()
        genome = dataset.readline().rstrip()
    print(*match(pattern, genome))

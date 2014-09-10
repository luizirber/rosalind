#! /usr/bin/env python

from __future__ import print_function

from collections import defaultdict, Counter


def clump(text, k, t):
    counter = defaultdict(int)
    for i, c in enumerate(text[:-k]):
        counter[text[i:i + k]] += 1

    clumps = Counter(counter)
    return [r[0] for r in clumps.most_common() if r[1] >= t]


if __name__ == "__main__":
    with open('data/rosalind_1d.txt', 'r') as dataset:
        text = dataset.readline().rstrip()
        k, L, t = [int(r) for r in dataset.readline().rstrip().split()]
    print(*clump(text, k, t))

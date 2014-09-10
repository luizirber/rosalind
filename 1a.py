#! /usr/bin/env python

from __future__ import print_function

from collections import defaultdict, Counter


def count(text, k):
    counter = defaultdict(int)
    for i, c in enumerate(text[:-k]):
        counter[text[i:i + k]] += 1

    return counter


if __name__ == "__main__":
    with open('data/rosalind_1a.txt', 'r') as dataset:
        text = dataset.readline().rstrip()
        k = int(dataset.readline().rstrip())
    common = Counter(count(text, k)).most_common()
    print(*[r[0] for r in common if r[1] == common[0][1]])

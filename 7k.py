#! /usr/bin/env python

from __future__ import print_function


from collections import defaultdict


def bwt_matches(last, patterns, alphabet="$ACGT"):
    first = sorted(last, key=lambda x: [alphabet.find(c) for c in x])

    first_idx = defaultdict(list)
    last_idx = defaultdict(list)
    for i, (cf, cl) in enumerate(zip(first, last)):
        first_idx[cf].append(i)
        last_idx[cl].append(i)

    matches = []
    for pattern in patterns:
        matching = [row for row in last_idx[pattern[0]]
                        if first[row] == pattern[1]]

        for prev, curr in zip(pattern[1:-1:], pattern[2::]):
            idx = [i for (i, row) in enumerate(first_idx[prev])
                     if row in matching]
            rows = [last_idx[prev][i] for i in idx]
            matching = [row for row in rows if first[row] == curr]

        matches.append(len(matching))

    return matches


if __name__ == "__main__":
    with open('data/rosalind_7k.txt', 'r') as dataset:
        text = dataset.readline().rstrip()
        patterns = dataset.readline().rstrip().split()
    print(*bwt_matches(text, patterns))

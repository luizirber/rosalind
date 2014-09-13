#! /usr/bin/env python

from __future__ import print_function


from collections import defaultdict


def naive_inverse_bwt(last_column, alphabet="$ACGT"):
    previous_column = sorted(last_column,
                             key=lambda x: [alphabet.find(c) for c in x])
    for i in range(len(last_column) - 1):
        next_column = sorted((t + f for t, f in zip(last_column, previous_column)),
                             key=lambda x: [alphabet.find(c) for c in x])
        previous_column = next_column
    return next_column[0][1:] + next_column[0][0]


def inverse_bwt(last, alphabet="$ACGT"):
    original = []
    first = sorted(last, key=lambda x: [alphabet.find(c) for c in x])

    first_idx = defaultdict(list)
    last_idx = defaultdict(list)
    for i, (cf, cl) in enumerate(zip(first, last)):
        first_idx[cf].append(i)
        last_idx[cl].append(i)

    original.append(first[0])
    original.append(last[0])

    next_row = first_idx[last[0]][0]
    original.append(last[next_row])

    for i in range(len(last) - 3):
        next_idx = next(i for (i, idx) in enumerate(last_idx[last[next_row]])
                        if idx == next_row)
        next_row = first_idx[last[next_row]][next_idx]
        original.append(last[next_row])

    return "".join(reversed(original))


if __name__ == "__main__":
    with open('data/rosalind_7j.txt', 'r') as dataset:
        text = dataset.readline().rstrip()
    print(inverse_bwt(text))

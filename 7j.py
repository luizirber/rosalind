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
    # calculate the first column
    # it's just the last column (bwt), but sorted in lexicographical order
    first = sorted(last, key=lambda x: [alphabet.find(c) for c in x])

    # small optimization: save the indexes for each character.
    # for example, idx['a'] == [3,4,5,8] are all positions
    # of char 'a' in the string.
    # To get the third occurrence of 'a' just need to access
    # idx['a'][2]
    first_idx = defaultdict(list)
    last_idx = defaultdict(list)
    for i, (cf, cl) in enumerate(zip(first, last)):
        first_idx[cf].append(i)
        last_idx[cl].append(i)

    original = []
    original.append(first[0])  # first[0] == '$'

    next_row = 0
    current_chr = last[next_row]
    original.append(current_chr)

    for i in range(len(last) - 2):
        next_idx = next(i for (i, idx) in enumerate(last_idx[current_chr])
                          if idx == next_row)
        next_row = first_idx[current_chr][next_idx]
        current_chr = last[next_row]
        original.append(current_chr)

    return "".join(reversed(original))


if __name__ == "__main__":
    with open('data/rosalind_7j.txt', 'r') as dataset:
        text = dataset.readline().rstrip()
    print(inverse_bwt(text))

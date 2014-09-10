#! /usr/bin/env python

from __future__ import print_function

from collections import defaultdict


def trie(patterns):
    adj_list = defaultdict(list)
    root = 1
    last_node = root

    for pattern in patterns:
        current_node = 1
        for ch in pattern:
            node = next((node for (node, letter)
                              in adj_list[current_node]
                              if letter == ch), None)
            if node:
                current_node = node
            else:
                last_node += 1
                adj_list[current_node].append((last_node, ch))
                current_node = last_node

    return adj_list


def trie_matching(pat_trie, text):
    pos = []

    for i in range(len(text)):
        current_node = 1
        for ch in text[i:]:

            node = next((node for (node, letter)
                              in pat_trie[current_node]
                              if letter == ch), None)
            if node:
                current_node = node
                if not pat_trie[current_node]:
                    # match, reached leaf node
                    pos.append(i)
                    break
                continue
            else:
                break
    return pos


if __name__ == "__main__":
    with open('data/rosalind_7b.txt', 'r') as dataset:
        text = dataset.readline().rstrip()
        patterns = [p.rstrip() for p in dataset.readlines()]

    pat_trie = trie(patterns)
    print(*trie_matching(pat_trie, text))

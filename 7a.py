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


if __name__ == "__main__":
    with open('data/rosalind_7a.txt', 'r') as dataset:
        patterns = [p.rstrip() for p in dataset.readlines()]

    for node, edges in trie(patterns).items():
        for edge, ch in edges:
            print(node, edge, ch)

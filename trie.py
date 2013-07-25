#!/usr/bin/env python

from __future__ import print_function
import os
from itertools import chain


def add_word(trie, word):
    if not trie:
        trie = {}
        for n, letter in enumerate(word, 1):
            trie[(n, n + 1)] = letter
    else:
        max_vertex = max(chain.from_iterable(e for e in trie))
        edges = {trie[e]: e for e in trie if e[0] == 1}
        for letter in word:
            if letter in edges:
                last = edges[letter][1]
                edges = {trie[e]: e for e in trie
                         if e[0] == last}
            else:
                if edges:
                    prev, _ = edges.popitem()[1]
                else:
                    prev = last
                max_vertex += 1
                trie[(prev, max_vertex)] = letter

                last = max_vertex
                edges = {}
    return trie


def write_dot(adj_list):
    '''
    digraph sample2 {
    A -> B [ label = "Edge A to B" ];
    B -> C [ label = "Edge B to C" ];
    A [label="Node A"];
    }'''
    with open('output.dot', 'w') as output:
        output.write('digraph trie {\n')
        for b, e in adj_list:
            line = '{0} -> {1} [ label = "{2}" ];\n'.format(
                b, e, adj_list[(b, e)])
            output.write(line)
        output.write('}\n')


if __name__ == "__main__":
    with open(os.path.join('data', 'rosalind_trie.txt')) as dataset:
        trie = None
        for s in [r.rstrip() for r in dataset.readlines()]:
            trie = add_word(trie, s)

        for b, e in sorted(trie):
            print(b, e, trie[(b, e)])

#        write_dot(trie)

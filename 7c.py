#! /usr/bin/env python

from __future__ import print_function

from collections import defaultdict


def write_dot(adj_list):
    '''
    digraph sample2 {
    A -> B [ label = "Edge A to B" ];
    B -> C [ label = "Edge B to C" ];
    A [label="Node A"];
    }'''
    with open('output.dot', 'w') as output:
        output.write('digraph trie {\n')
        for b in adj_list:
            for e, letter in adj_list[b]:
                line = '{0} -> {1} [ label = "{2}" ];\n'.format(b, e, letter)
                output.write(line)
        output.write('}\n')


def suffix_trie(text):
    adj_list = defaultdict(list)
    node_props = {}
    root = 1
    last_node = root

    for i in reversed(range(len(text))):
        current_node = 1
        for ch in text[i:]:
            node = next((node for (node, letter)
                              in adj_list[current_node]
                              if letter == ch), None)
            if node:
                current_node = node
            else:
                last_node += 1
                adj_list[current_node].append((last_node, ch))
                current_node = last_node

            #if ch == '$':
            #    node_props[current_node] = i

    return adj_list, None #, node_props


def backtrace(parent, start, end):
    path = [end]
    while path[-1] != start:
        path.append(parent[path[-1]])
    path.reverse()
    return path


def find_longest_repeat(text):
    suf_trie, _ = suffix_trie(text + '$')
    branches = [node for node in suf_trie
                if len(suf_trie[node]) > 1 and (node != 1)]
    start = 1
    parent = {}
    queue = []
    queue.append(start)
    longest_path = []
    while queue:
        node = queue.pop(0)
        if not branches:
            break

        for adjacent, letter in suf_trie.get(node, []):
            parent[adjacent] = node
            queue.append(adjacent)
        if node in branches:
            new_path = backtrace(parent, start, node)
            if len(new_path) > len(longest_path):
                longest_path = new_path
            branches.remove(node)

    longest = []
    for start, end in zip(longest_path[:-1], longest_path[1:]):
        for node, letter in suf_trie[start]:
            if node == end:
                longest.append(letter)
                break

    return "".join(longest)

if __name__ == "__main__":
    with open('data/rosalind_7c.txt', 'r') as dataset:
        text = dataset.readline().rstrip()
    print(find_longest_repeat(text))

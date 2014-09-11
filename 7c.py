#! /usr/bin/env python

from __future__ import print_function


from suftree import suffix_tree, str_from_path, path_to_root


def find_longest_repeat(text):
    suf_tree = suffix_tree(text + '$')
    candidates = []

    start = suf_tree
    queue = []
    queue.append(start)
    while queue:
        node = queue.pop(0)
        for key, (_, v) in node.children.items():
            queue.append(v)
        if len(node.children) > 1:
            candidates.append(node)

    longest = ""
    for c in candidates:
        c_str = str_from_path(path_to_root(c, suf_tree), text)
        if len(c_str) > len(longest):
            longest = c_str

    return longest


if __name__ == "__main__":
    with open('data/rosalind_7c.txt', 'r') as dataset:
        text = dataset.readline().rstrip()
    print(find_longest_repeat(text))

#!/usr/bin/env python

from __future__ import print_function
import os


class Newick(object):
    def __init__(self, clade, children, weight=1):
        self.clade = clade
        self.children = children
        self.weight = weight

    @classmethod
    def parse(cls, text):
        text = text.strip().rstrip(';')
        if text.count('(') == 0:
            return Newick.parse_clade(text)
        close_posn = text.rfind(')')
        subtrees = []
        plevel = 0
        prev = 1
        for posn in range(1, close_posn):
            if text[posn] == '(':
                plevel += 1
            elif text[posn] == ')':
                plevel -= 1
            elif text[posn] == ',' and plevel == 0:
                subtrees.append(text[prev:posn])
                prev = posn + 1
        subtrees.append(text[prev:close_posn])
        clade = Newick.parse_clade(text[close_posn + 1:])
        clade.children = [Newick.parse(st) for st in subtrees]
        return clade

    @classmethod
    def parse_clade(cls, text):
        if ':' in text:
            tag, weight = text.split(':')
        else:
            tag, weight = text, 1
        return cls(tag, [], weight=int(weight))

    def path(self, n1, path=[]):
        if n1 == self.clade:
            return path
        if not self.children:
            return None
        for c in self.children:
            result = c.path(n1, path + [c])
            if result:
                return result

    def distance(self, n1, n2=None, weighted=False):
        p1 = self.path(n1)
        if n2 is None:
            return len(p1)
        p2 = self.path(n2)
        same = 0
        same_path = []
        while same < min(len(p1), len(p2)) and p1[same] == p2[same]:
            same_path.append(p1[same])
            same += 1
        return (sum(p.weight for p in p1) +
                sum(p.weight for p in p2) -
                2 * sum(s.weight for s in same_path))

    def __repr__(self):
        return self.clade


def parse_file(ifile):
    trees = []
    nodes = []
    running = True
    while running:
        line = ifile.readline().strip()
        if line:
            trees.append(Newick.parse(line))
            nodes.append(ifile.readline().rstrip().split())
            running = ifile.readline()
        else:
            running = False

    return trees, nodes


if __name__ == "__main__":
    with open(os.path.join('data', 'rosalind_nwck.txt')) as dataset:
        trees, nodes = parse_file(dataset)
        print(*[int(t.distance(*n)) for t, n in zip(trees, nodes)])

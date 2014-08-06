#!/usr/bin/env python

from __future__ import print_function, division
import os
from collections import defaultdict


def degree(graph, v):
    return len(graph[v])


if __name__ == "__main__":
    with open(os.path.join('data', 'rosalind_deg.txt')) as dataset:
        vertices, edges = [int(r) for r in dataset.readline().split()]
        graph = defaultdict(list)
        for line in dataset:
            line = line.strip()
            if line:
                h, t = [int(r) for r in line.split()]
                graph[h].append(t)
                graph[t].append(h)

        print(*[degree(graph, v) for v in range(1, vertices + 1)])

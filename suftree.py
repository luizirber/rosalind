#! /usr/bin/env python
# Based on http://www.allisons.org/ll/AlgDS/Tree/Suffix/


INF = 1e20


def suffix_tree(original_text):
    text = original_text + '$'
    root = State()
    bt = State()

    for i in range(0, len(text)):
        bt.add_transition(text, i, i, root)

    root.sLink = bt
    s = root
    k = 0

    for i in range(0, len(text)):
        s, k = update(text, root, s, k, i)
        s, k = canonize(text, s, k, i)

    return root


class State(object):
    def __init__(self):
        self.isLeaf = True
        self.children = {}
        self.sLink = None
        self.parent = None

    def add_transition(self, text, left, right, s):
        self.children[text[left]] = ((left, right), s)
        self.isLeaf = False

    def __getitem__(self, key):
        return self.children.get(key, None)

    def __str__(self):
        return "State(child: %s, sLink: %s)" % (
                    "".join(self.children.keys()),
                    self.sLink)

    def __repr__(self):
        return str(self)


def update(text, root, s, k, i):
    oldr = root
    endpoint, r = test_and_split(text, s, k, i-1, text[i])

    while not endpoint:
        new_state = State()
        r.add_transition(text, i, INF, new_state)
        new_state.parent = r
        if oldr != root:
            oldr.sLink = r

        oldr = r
        s, k = canonize(text, s.sLink, k, i - 1)
        endpoint, r = test_and_split(text, s, k, i - 1, text[i])

    if oldr != root:
        oldr.sLink = s

    return s, k


def canonize(text, s, k, p):
    if p < k:
        return s, k

    (k1, p1), s1 = s[text[k]]
    while (p1 - k1) <= (p - k):
        k += p1 - k1 + 1
        s = s1
        if k <= p:
            (k1, p1), s1 = s[text[k]]

    return s, k


def test_and_split(text, s, k, p, t):
    if k <= p:
        (k1, p1), s1 = s[text[k]]

        if t == text[k1 + p - k + 1]:
            return True, s
        else:
            r = State()
            s.add_transition(text, k1, k1 + p - k, r)
            r.parent = s
            r.add_transition(text, k1 + p - k + 1, p1, s1)
            s1.parent = r
            return False, r
    else:
        try:
            return s[t] is not None, s
        except TypeError:
            return True, s


def path_to_root(node, root):
    path = [node]
    current = node
    while current != root and current is not None:
        current = current.parent
        path.append(current)
    path.reverse()
    return path


def str_from_path(path, text):
    edges = []
    for start, end in zip(path[:-1:], path[1::]):
        edge = next((b, e) for c, ((b, e), s) in start.children.items()
                           if s == end)
        edges.append(edge)
    return "".join(text[edge[0]:edge[1] + 1] for edge in edges)

#!/usr/bin/env python

from __future__ import print_function
import os


def fib(n, k, fib_memo={}):
    args = (n, k)
    if args in fib_memo:
        return fib_memo[args]

    if n == 1 or n == 2:
        ans = 1
    else:
        ans = fib(n - 2, k, fib_memo) * k + fib(n - 1, k, fib_memo)

    fib_memo[args] = ans
    return ans


if __name__ == "__main__":
    with open(os.path.join('data', 'rosalind_fib.txt')) as dataset:
        n, k = dataset.read().split()
        print(fib(int(n), int(k)))

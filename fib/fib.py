import os

memo = {}
def fib(n, k):
    args = (n, k)
    if args in memo:
        return memo[args]

    if n == 1 or n == 2:
        ans = 1
    else:
        ans = fib(n - 2, k) * k + fib(n - 1, k)

    memo[args] = ans
    return ans


PROJPATH = os.path.abspath(
    os.path.join(os.path.dirname(__file__), os.path.pardir))

N, K = open(os.path.join(PROJPATH, 'data', 'rosalind_fib.txt')).read().split()

print fib(int(N), int(K))

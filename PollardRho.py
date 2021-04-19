#!/usr/bin/python3

from math import gcd
import sys


alpha, beta, N = map(int, sys.stdin.read().split())

def f(x):
    if x % 3 == 2:
        return (beta * x) % N
    if x % 3 == 0:
        return (x * x) % N
    return (alpha * x) % N

def g(x, n):
    if x % 3 == 2:
        return n
    if x % 3 == 0:
        return (2 * n) % (N - 1)
    return (n + 1) % (N - 1)

def h(x, n):
    return g(-x % 3, n)

a0, b0, x0, a1, b1, x1 = 0, 0, 1, 0, 0, 1
while True:
    a0 = g(x0, a0)
    b0 = h(x0, b0)
    x0 = f(x0)
    a1 = g(f(x1), g(x1, a1))
    b1 = h(f(x1), h(x1, b1))
    x1 = f(f(x1))
    if x0 == x1:
        assert (pow(alpha, a1, N) * pow(beta, b1, N)) % N == (pow(alpha, a0, N) * pow(beta, b0, N)) % N
        r = (b0 - b1) % (N-1)
        if r == 0:
            print("No solution found")
            break
        g = gcd(r, N-1)
        r = r // g
        a = (a1 - a0) // g
        n = (N-1) // g
        x = ((pow(r, -1, n) * a) % n)
        y = pow(alpha, x, N)
        d = pow(alpha, n, N)
        for i in range(g):
            if y == beta:
                print(x + i*n)
                break
            y *= d
            y %= N
        break
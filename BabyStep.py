#!/usr/bin/python3

from math import sqrt
import sys

alpha, beta, N = map(int, sys.stdin.read().split())

m = int(sqrt(N)) + 1
table = {}
k = 1
for i in range(m):
    table[k] = i
    k *= alpha
    k %= N
y = beta
am = pow(alpha, -m, N)
for i in range(m):
    if y in table:
        print(i * m + table[y])
        break
    y *= am
    y %= N
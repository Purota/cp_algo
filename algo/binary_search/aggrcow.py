#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
AGGRCOW - Aggressive cows
https://www.spoj.com/problems/AGGRCOW/

Modified input:
First line contains an integer t - the number of test cases
First line of test case contains two integers N - number of stalls - and C - number of cows -
Second line of test case contains N integers representing stalls' positions
"""

def can_place_cows(A, C, d):
    C -= 1 # First cow is automatically placed in the first stall
    i = 1
    last = 0
    while C > 0:
        if i >= len(A):
            return False
        if A[i] - A[last] >= d:
            C -= 1
            last = i
        i += 1
    return True

def binary_search(A, C):
    low = 1
    high = A[-1] - A[0]
    while low < high:
        mid = low + (high - low + 1) // 2
        if can_place_cows(A, C, mid):
            low = mid
        else:
            high = mid - 1
    return low

t = int(input())

for _ in range(t):
    N, C = map(int, input().split())
    X = [int(x_i) for x_i in input().split()]
    X.sort()
    best = binary_search(X, C)
    print(best)
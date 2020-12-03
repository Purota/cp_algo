#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Problem B from ARC 109
https://atcoder.jp/contests/arc109/tasks/arc109_b

Modified input:
First line contains an integer t - the number of test cases
Then t lines containing an integer n
"""

def is_enough(k, n):
    r = n + 1
    s = r - k
    sum_1_to_n = n * (n + 1) // 2
    sum_s_to_r = (r * (r + 1) - s * (s + 1)) // 2
    return sum_s_to_r >= sum_1_to_n

def binary_search(low, high, p):
    n = high - 1
    while low < high:
        mid = low + (high - low) // 2
        if p(mid, n):
            high = mid
        else:
            low = mid + 1
    return low

t = int(input())

for _ in range(t):
    n = int(input())
    ind = binary_search(1, n + 1, is_enough)
    print(ind)
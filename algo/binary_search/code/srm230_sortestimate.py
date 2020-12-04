#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
SRM 230 - SortEstimate
https://community.topcoder.com/stat?c=problem_statement&pm=3561&rd=6519

Input:
First line contains an integer t - the number of test cases
Each case test contains two integers c - the cost - and m - the maximum time allowed -
"""
import math

def compute_time(c, n):
    return c * n * math.log2(n)

def how_many(c, time):
    low = 0
    high = time
    while high - low > 1e-9:
        old_low, old_high = low, high
        mid = (high + low) / 2
        if compute_time(c, mid) <= time:
            low = mid
        else:
            high = mid
        if old_low == low and old_high == high:
            break
    return low

t = int(input())
for _ in range(t):
    c, m = map(int, input().split())
    max_sort = how_many(c, m)
    print("{:.9f}".format(max_sort))

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
SRM 277 - UnionOfIntervals
https://community.topcoder.com/stat?c=problem_statement&pm=4823&rd=8074

Input:
First line contains an integer t - the number of test cases
The first line of each test case contains two integer n - the index of the value - and s - the size of lower bounds and upper bounds arrays -
The second line of each test case contains s integers forming l - the array of lower bounds -
The third line of each test case contains s integers forming u - the array of upper bounds -
"""
import math

def nth_element(lower_bound, upper_bound, n):
    n += 1
    low = min(lower_bound)
    high = max(upper_bound)
    while low < high:
        mid = low + (high - low) // 2
        count = 0
        for i, lower in enumerate(lower_bound):
            if lower <= mid:
                upper = upper_bound[i]
                if upper < mid:
                    count += upper - lower + 1
                else:
                    count += mid - lower + 1
        if count >= n:
            high = mid
        else:
            low = mid + 1
    return low

t = int(input())

for _ in range(t):
    n, s = map(int, input().split())
    l = [int(v) for v in input().split()]
    u = [int(v) for v in input().split()]
    el = nth_element(l, u, n)
    print(el)
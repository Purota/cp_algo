#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def is_sorted(a):
    last = a[0]
    for i in range(1, len(a)):
        if a[i] < last:
            return False
        last = a[i]
    return True

def sequence_and_swaps(a, x):
    if is_sorted(a):
        return 0
    count = 0
    for i in range(len(a)):
        if a[i] > x:
            a[i], x = x, a[i]
            count += 1
        if is_sorted(a[i:]):
            break
    if is_sorted(a):
        return count
    return -1

t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    a = [int(a_i) for a_i in input().split()]
    ans = sequence_and_swaps(a, x)
    print(ans)
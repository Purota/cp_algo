#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def jumps(x):
    k = 0
    count = 0
    while k < x:
        count += 1
        k += count
    if k == x + 1:
        count += 1
    return count

t = int(input())
for _ in range(t):
    x = int(input())
    ans = jumps(x)
    print(ans)
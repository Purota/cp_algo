#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def black_square(a, s):
    total = 0
    for s_i in s:
        total += a[int(s_i) - 1]
    return total

a = [int(a_i) for a_i in input().split()]
s = input()
ans = black_square(a, s)
print(ans)

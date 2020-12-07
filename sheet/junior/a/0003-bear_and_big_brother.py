#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def bear_and_big_brother(a, b):
    year = 0
    while a <= b:
        year += 1
        a *= 3
        b *= 2
    return year

a, b = map(int, input().split())
ans = bear_and_big_brother(a, b)
print(ans)

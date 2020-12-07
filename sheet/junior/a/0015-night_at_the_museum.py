#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def night_at_the_museum(s):
    total = 0
    last = 'a'
    for c in s:
        dist = abs(ord(last) - ord(c))
        total += min(dist, 26 - dist)
        last = c
    return total

s = input()
ans = night_at_the_museum(s)
print(ans)

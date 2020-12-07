#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def word(s):
    lower_count = 0
    for c in s:
        if ord('a') <= ord(c) <= ord('z'):
            lower_count += 1
    upper_count = len(s) - lower_count
    if upper_count > lower_count:
        return s.upper()
    else:
        return s.lower()

s = input()
ans = word(s)
print(ans)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def colorful_stones(s, t):
    i = 0
    for t_i in t:
        if t_i == s[i]:
            i += 1
    return i + 1

s = input()
t = input()
ans = colorful_stones(s, t)
print(ans)

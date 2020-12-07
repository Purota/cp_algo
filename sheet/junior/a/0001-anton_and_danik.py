#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def anton_and_danik(s, n):
    a = 0
    for c in s:
        if c == 'A':
            a += 1
    d = n - a
    if a > d:
        return "Anton"
    elif d > a:
        return "Danik"
    else:
        return "Friendship"

n = int(input())
s = input()
ans = anton_and_danik(s, n)
print(ans)

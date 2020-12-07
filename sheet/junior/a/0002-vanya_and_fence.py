#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def vanya_and_fence(a, h):
    width = 0
    for a_i in a:
        width += 1 if a_i <= h else 2
    return width

n, h = map(int, input().split())
a = [int(a_i) for a_i in input().split()]
ans = vanya_and_fence(a, h)
print(ans)

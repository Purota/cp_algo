#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def die_roll(y, w):
    num = 6 - max(y, w) + 1
    denom = 6
    if num % 2 == 0:
        num //= 2
        denom //= 2
    if num % 3 == 0:
        num //= 3
        denom //= 3
    return "{}/{}".format(num, denom)

y, w = map(int, input().split())
ans = die_roll(y, w)
print(ans)

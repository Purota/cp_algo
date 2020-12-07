#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def police_recruits(e):
    count = 0
    p = 0
    for e_i in e:
        if p + e_i < 0:
            count += 1
        else:
            p += e_i
    return count

n = int(input())
e = [int(e_i) for e_i in input().split()]
ans = police_recruits(e)
print(ans)

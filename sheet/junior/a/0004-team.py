#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def team(p):
    return sum(p) > 1

n = int(input())
ans = 0
for _ in range(n):
    p = [int(pvt) for pvt in input().split()]
    ans += team(p)
print(ans)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def games(ha, n):
    total = 0
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if ha[i][0] == ha[j][1]:
                total += 1
    return total

n = int(input())
ha = [[int(h_ai) for h_ai in input().split()] for _ in range(n)]
ans = games(ha, n)
print(ans)

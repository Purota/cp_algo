#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def beautiful_matrix(m):
    for i in range(5):
        for j in range(5):
            if m[i][j] == 1:
                return abs(i - 2) + abs(j - 2)

m = [ [int(v) for v in input().split()] for _ in range(5) ]
ans = beautiful_matrix(m)
print(ans)

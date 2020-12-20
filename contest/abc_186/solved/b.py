#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import io, os

input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

def blocks_on_grid(A, h, w):
    total = 0
    a_min = 100
    for row in A:
        total += sum(row)
        a_min = min(a_min, min(row))
    return total - (h * w) * a_min

h, w = map(int, input().split())
A = [[int(a_i) for a_i in input().split()] for _ in range(h)]
ans = blocks_on_grid(A, h, w)
print(ans)
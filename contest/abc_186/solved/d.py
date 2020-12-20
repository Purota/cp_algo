#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import io, os

input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

def sum_of_difference(a, n): 
    a.sort() 
    res = 0
    sum = 0
    for i in range(n): 
        res += (a[i] * i - sum) 
        sum += a[i]
    return res

n = int(input())
a = [int(a_i) for a_i in input().split()]
ans = sum_of_difference(a, n)
print(ans)
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math

def check_k(a, N, k):
    last = 0
    for a_i in a:
        diff = a_i - last - 1
        if 0 < diff < k:
            return False 
        last = a_i
    if N - last == 0:
        return True
    return N - last >= k

def find_k(a, N):
    low = 1
    high = N
    while high > low:
        mid = low + (high - low + 1) // 2
        if check_k(a, N, mid):
            low = mid
        else:
            high = mid - 1
    return low

def stamp(a, N):
    a.sort()
    k = find_k(a, N)
    last = 0
    count = 0
    for a_i in a:
        count += math.ceil((a_i - last - 1) / k)
        last = a_i
    count += math.ceil((N - last) / k)
    return count

N, M = map(int, input().split())
a = [int(a_i) for a_i in input().split()]
ans = stamp(a, N)
print(ans)
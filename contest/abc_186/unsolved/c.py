#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import io, os

input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

def unlucky_7(n):
    count = 0
    for i in range(n + 1):
        if '7' in str(i):
            count += 1
        elif '7' in oct(i):
            count += 1
    return n - count

n = int(input())
ans = unlucky_7(n)
print(ans)
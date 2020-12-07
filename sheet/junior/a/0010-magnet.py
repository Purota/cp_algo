#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import io, os

input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline

def magnet(m, last):
    return m != last

n = int(input())
ans = 0
last = ''
for _ in range(n):
    m = input()
    ans += magnet(m, last)
    last = m
print(ans)
